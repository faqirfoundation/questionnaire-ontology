"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from src.questionnaire_ontology.datamodel import QoQuestionnaire, QoQuestionnaireResponse

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            obj1 = yaml_loader.load(path, target_class=QoQuestionnaire)
            assert obj1
        for path in EXAMPLE_FILES:
            obj2 = yaml_loader.load(path, target_class=QoQuestionnaireResponse)
            assert obj2
