#!/usr/bin/env python3
"""
Post-processing script for LinkML-generated OWL output.
1. Replaces 'schema1' prefix with 'schema'
2. Replaces 'ssn1' prefix with 'ssn'
3. Converts 'qo:xxx_yyy' resources into 'xxx:yyy' URIs (e.g., qo:prov_type -> prov:type)
"""

from pathlib import Path
import sys
import re
import rdflib

# Base URI for the local 'qo' namespace
QO_BASE = "https://ns.faqir.org/q-o#"

def main():
    if len(sys.argv) < 2:
        print("Usage: python post_process_owl.py <path_to_owl_file>")
        sys.exit(1)

    owl_file = Path(sys.argv[1])
    if not owl_file.exists():
        print(f"File not found: {owl_file}")
        sys.exit(1)

    g = rdflib.Graph()
    g.parse(owl_file, format="ttl")

    # -------------------------------------------------------------------------
    # 1 & 2. Fix Prefixes (schema1 -> schema, ssn1 -> ssn)
    # -------------------------------------------------------------------------
    # Reset RDFLib's namespace manager bindings
    ns_mgr = rdflib.namespace.NamespaceManager(rdflib.Graph())
    
    # Copy all namespaces except schema1 and ssn1
    for prefix, ns in list(g.namespaces()):
        if prefix in ("schema1", "ssn1"):
            continue
        ns_mgr.bind(prefix, ns, override=True)

    # Bind schema and ssn cleanly
    ns_mgr.bind("schema", rdflib.Namespace("http://schema.org/"), override=True)
    ns_mgr.bind("ssn", rdflib.Namespace("http://www.w3.org/ns/ssn/"), override=True)

    g.namespace_manager = ns_mgr

    # Serialize updated Graph back to Turtle
    g.serialize(owl_file, format="ttl")
    print(f"Successfully post-processed {owl_file}")

    # -------------------------------------------------------------------------
    # 3. Convert 'qo:xxx_yyy' -> 'xxx:yyy'
    # -------------------------------------------------------------------------
    # Pattern to match URIs ending with qo:xxx_yyy
    pattern = re.compile(rf"^{re.escape(QO_BASE)}([a-zA-Z0-9]+)_([a-zA-Z0-9_]+)$")

    triples_to_modify = []

    for s, p, o in g:
        new_s = s
        new_p = p
        new_o = o

        # Check Subject
        if isinstance(s, rdflib.URIRef):
            match = pattern.match(str(s))
            if match:
                prefix, local_name = match.groups()
                ns = dict(g.namespaces()).get(prefix)
                if ns:
                    new_s = rdflib.URIRef(f"{ns}{local_name}")

        # Check Predicate
        if isinstance(p, rdflib.URIRef):
            match = pattern.match(str(p))
            if match:
                prefix, local_name = match.groups()
                ns = dict(g.namespaces()).get(prefix)
                if ns:
                    new_p = rdflib.URIRef(f"{ns}{local_name}")

        # Check Object
        if isinstance(o, rdflib.URIRef):
            match = pattern.match(str(o))
            if match:
                prefix, local_name = match.groups()
                ns = dict(g.namespaces()).get(prefix)
                if ns:
                    new_o = rdflib.URIRef(f"{ns}{local_name}")

        if (new_s, new_p, new_o) != (s, p, o):
            triples_to_modify.append(((s, p, o), (new_s, new_p, new_o)))
    
    # Apply transformations
    for old_triple, new_triple in triples_to_modify:
        g.remove(old_triple)
        g.add(new_triple)

    # Serialize updated Graph back to Turtle
    g.serialize(owl_file, format="ttl")
    print(f"Successfully post-processed {owl_file}")

if __name__ == "__main__":
    main()