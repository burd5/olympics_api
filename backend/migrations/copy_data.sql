\copy olympics (id, name, sex, age, height, weight, team, noc, games, year, season, city, sport, event, medal) FROM 'athlete_events.csv' DELIMITER ',' CSV HEADER NULL 'NA';

\copy athletes (id, name, sex, age, height, weight, team) FROM 'backend/data/athletes.csv' DELIMITER ',' CSV HEADER NULL '';
\copy events (sport, event) FROM 'backend/data/events.csv' DELIMITER ',' CSV HEADER NULL '';
\copy games (games, year, season, city) FROM 'backend/data/games.csv' DELIMITER ',' CSV HEADER NULL '';
\copy teams (team, noc) FROM 'backend/data/teams.csv' DELIMITER ',' CSV HEADER NULL 'NA';
\copy results (athlete_id, games, team, event, medal) FROM 'backend/data/results.csv' DELIMITER ',' CSV HEADER NULL '';