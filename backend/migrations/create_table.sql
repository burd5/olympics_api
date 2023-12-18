DROP TABLE IF EXISTS athletes;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS results;

CREATE TYPE sex AS ENUM('M','F', 'NA');
CREATE TYPE medal_ops AS ENUM('Gold', 'Silver', 'Bronze', 'NA');

CREATE TABLE IF NOT EXISTS athletes(
    id integer,
    name VARCHAR(255),
    sex sex,
    age float,
    height float,
    weight float,
    team VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS teams(
    team VARCHAR(255),
    noc VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS events(
    sport VARCHAR(255),
    event VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS games(
    games VARCHAR(255),
    year integer,
    season VARCHAR(255),
    city VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS results(
    athlete_id integer,
    games VARCHAR(255),
    team VARCHAR(255),
    event VARCHAR(255),
    medal medal_ops
);