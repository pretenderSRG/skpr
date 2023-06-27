CREATE TABLE netflix (
    show_id TEXT,
    type TEXT,
    title TEXT,
    director TEXT,
    cast Text,
    country TEXT,
    date_added DATETIME,
    release_year INTEGER,
    rating TEXT,
    duration TEXT,
    duration_type TEXT,
    listed_in TEXT,
    description TEXT
);
-- new formats
CREATE TABLE directors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);
CREATE TABLE actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT name VARCHAR(100) NOT NULL
);
CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category VARCHAR(100) NOT NULL
);
CREATE TABLE duration_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL
);
CREATE TABLE show_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    duration INTEGER NOT NULL,
    FOREIGN KEY (type_id) REFERENCES duration_type(id)
);
CREATE TABLE show_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(40),
);
CREATE TABLE shows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_id INTEGER,
    title TEXT,
    country TEXT,
    date_added DATETIME,
    release_year INTEGER,
    rating TEXT,
    duration_id INTEGER -- duration TEXT,
    -- duration_type TEXT,
    description TEXT FOREIGN KEY (duration_id) REFERENCES show_info(id) FOREIGN KEY (type_id) REFERENCES show_type(id)
);
CREATE TABLE show_director (
    show_id INTEGER,
    director_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (director_id) REFERENCES directors(id)
);
CREATE TABLE show_actors (
    show_id INTEGER,
    actors_id INTEGER,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (actors_id) REFERENCES actors(id)
);
CREATE TABLE show_categories (
    show_id INTEGER,
    category_id INTEGER,
    FOREIGN key (show_id) REFERENCES shows(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);