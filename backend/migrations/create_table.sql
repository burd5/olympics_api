DROP TABLE IF EXISTS olympics;

CREATE TYPE sex AS ENUM('M','F', 'NA');
CREATE TYPE medal_ops AS ENUM('Gold', 'Silver', 'Bronze', 'NA');


CREATE TABLE IF NOT EXISTS olympics(
    id integer,
    name VARCHAR(255),
    sex sex,
    age integer,
    height float,
    weight float,
    team VARCHAR(255),
    noc VARCHAR(255),
    games VARCHAR(255),
    year integer,
    season VARCHAR(255),
    city VARCHAR(255),
    sport VARCHAR(255),
    event VARCHAR(255),
    medal medal_ops
)


-- \copy olympics (id, name, sex, age, height, weight, team, noc, games, year, season, city, sport, event, medal) FROM 'athlete_events.csv' DELIMITER ',' CSV HEADER NULL 'NA';