-- # Class: "Vault" Description: "The FAQIR healthdata vault"
--     * Slot: id Description: The unique identifier for a vault.
--     * Slot: birthdate Description: The date of birth
--     * Slot: full_name_id Description: 
--     * Slot: weight_id Description: 
-- # Class: "FullName" Description: "Structured full name"
--     * Slot: id Description: 
--     * Slot: first_name Description: Given or first name
--     * Slot: middle_name Description: Middle name
--     * Slot: family_name Description: Family or last name
-- # Class: "WeightC" Description: "Weight"
--     * Slot: id Description: 
--     * Slot: type Description: 
--     * Slot: mass_in_kg Description: 

CREATE TABLE "FullName" (
	id INTEGER NOT NULL, 
	first_name TEXT, 
	middle_name TEXT, 
	family_name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "WeightC" (
	id INTEGER NOT NULL, 
	type VARCHAR(20) NOT NULL, 
	mass_in_kg FLOAT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Vault" (
	id TEXT NOT NULL, 
	birthdate DATE, 
	full_name_id INTEGER, 
	weight_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(full_name_id) REFERENCES "FullName" (id), 
	FOREIGN KEY(weight_id) REFERENCES "WeightC" (id)
);