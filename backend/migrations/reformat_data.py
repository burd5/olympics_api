import pandas as pd
import os  
os.makedirs('/Users/austinburdette/Documents/jigsaw/olympics_api/data/', exist_ok=True)  



athletes = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/athlete_events.csv', usecols=['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team'])
athletes.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/athletes.csv', index=False) 

teams = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/athlete_events.csv', usecols=['Team', 'NOC'])
teams.drop_duplicates(subset=None, inplace=True)
teams.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/teams.csv', index=False) 

events = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/athlete_events.csv', usecols=['Sport', 'Event'])
events.drop_duplicates(subset=None, inplace=True)
events.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/events.csv', index=False) 

games = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/athlete_events.csv', usecols=['Games', 'Year', 'Season', 'City'])
games.drop_duplicates(subset=None, inplace=True)
games.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/games.csv', index=False) 

results = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/athlete_events.csv', usecols=['ID', 'Team', 'Games', 'Event', 'Medal'])
results.drop_duplicates(subset=None, inplace=True)
results.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/backend/data/results.csv', index=False) 
