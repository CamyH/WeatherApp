DROP TABLE if EXISTS data;

CREATE TABLE data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    temperature INTEGER NOT NULL,
    feels_like INTEGER NOT NULL,
    wind_speed REAL NOT NULL,
    current_weather_type TEXT NOT NULL,
    weather_description TEXT NOT NULL,
    sunrise TEXT NOT NULL,
    sunset TEXT NOT NULL,
    uv_index REAL NOT NULL,
    datetime TEXT NOT NULL
);