import pandas as pd
import os  
os.makedirs('/Users/austinburdette/Documents/jigsaw/olympics_api/data/', exist_ok=True)  



athletes = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/athlete_events.csv', usecols=['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team'])
athletes.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/athletes.csv', index=False) 

teams = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/athlete_events.csv', usecols=['Team', 'NOC'])
teams.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/teams.csv', index=False) 

events = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/athlete_events.csv', usecols=['Sport', 'Event'])
events.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/events.csv', index=False) 

games = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/athlete_events.csv', usecols=['Games', 'Year', 'Season', 'City'])
games.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/games.csv', index=False) 

results = pd.read_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/athlete_events.csv', usecols=['ID', 'Games', 'Team', 'Event', 'Medal'])
results.to_csv('/Users/austinburdette/Documents/jigsaw/olympics_api/data/results.csv', index=False) 
