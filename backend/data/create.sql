CREATE TABLE Environment (
    id INTEGER PRIMARY KEY,
    humidity REAL,        
    temperature REAL,      
    pressure REAL,         
    ph_value REAL,         
    light_intensity REAL,  
    timestamp DATETIME     
);


CREATE TABLE User (
    id TEXT PRIMARY KEY,
    'password' TEXT NOT NULL,
    primer INTEGER DEFAULT 0
)


CREATE TABLE environment (
    id INTEGER PRIMARY KEY,
    devicename TEXT,
    crowd INTEGER,
    abright INTEGER,
    atemp REAL,
    ahum REAL,
    timestamp DATETIME
);

    tocloud INTEGER DEFAULT 0