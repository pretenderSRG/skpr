CREATE TABLE colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(40) NOT NULL
);
CREATE TABLE outcome_dates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    outcome_month DATE,
    outcome_year DATE
);
CREATE TABLE outcome_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    outcome_subtype VARCHAR(100),
    outcome_type VARCHAR(100),
    outcome_date_id INTEGER,
    age_upon_outcome INTEGER,
    FOREIGN KEY (outcome_date_id) REFERENCES outcome_dates(id)
);
CREATE TABLE colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(100)
);
CREATE TABLE animals_1 (
    index INTEGER PRIMARY KEY AUTOINCREMENT,
    animal_id VARCHAR(100) NOT NULL,
    animal_type VARCHAR(100),
    'name' VARCHAR(100),
    breed VARCHAR(100),
    color_id INTEGER,
    date_of_birth DATE,
    outcome_info_id INTEGER,
    FOREIGN KEY (color_id) REFERENCES colors(id),
    FOREIGN KEY (outcome_info_id) REFERENCES outcome_info(id)
)