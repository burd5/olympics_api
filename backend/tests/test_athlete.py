from backend.api.models import *
import pytest
from .test_db_utilities import *

@pytest.fixture
def build_results():
    drop_all_tables(conn, cursor)
    athlete = save(Athlete(id = 94406, name = "Michael Fred Phelps, II", sex =  "M", age =  23.0, height = 193.0, weight =  91.0, team = "United States"), conn, cursor)
    result1 = save(Result(athlete_id = 94406, team = 'United States', games = '2000 Summer', event = "Swimming Men's 200 metres Butterfly", medal = None), conn, cursor) 
    result2 = save(Result(athlete_id = 94406, team = 'United States', games = '2016 Summer', event = "Swimming Men's 100 metres Butterfly", medal = 'Silver'), conn, cursor)
    yield athlete
    drop_all_tables(conn, cursor)

@pytest.fixture
def build_events():
    drop_all_tables(conn, cursor)
    athlete = save(Athlete(id = 94406, name = "Michael Fred Phelps, II", sex =  "M", age =  23.0, height = 193.0, weight =  91.0, team = "United States"), conn, cursor)
    result1 = save(Result(athlete_id = 94406, event = "Swimming Men's 100 metres Butterfly", games = "2016 Summer", medal = "Silver", team = "United States"), conn, cursor)
    result2 = save(Result(athlete_id = 94406, event = "Swimming Men's 200 metres Butterfly", games = "2000 Summer", medal = None, team = "United States"), conn, cursor)
    event1 = save(Event(event = "Swimming Men's 100 metres Butterfly", sport = "Swimming"), conn, cursor)
    event2 = save(Event(event = "Swimming Men's 200 metres Butterfly", sport = "Swimming"), conn, cursor)

    yield athlete
    drop_all_tables(conn, cursor)

@pytest.fixture
def build_athletes():
    drop_all_tables(conn, cursor)
    athlete1 = save(Athlete(id = 94406, name = "Michael Fred Phelps, II", sex =  "M", age =  23.0, height = 193.0, weight =  91.0, team = "United States"), conn, cursor)
    athlete2 = save(Athlete(id = 702, name = "Ronny Ackermann", sex = "M", age = 20.0, height = 184.0, weight = 69.0, team = "Germany"), conn, cursor)
    athlete3 = save(Athlete(id = 1526, name = "Samir At Sad", sex = "M", age = 26.0, height = 167.0, weight = 65.0, team = "France"), conn, cursor)

    yield [athlete1, athlete2, athlete3]
    drop_all_tables(conn, cursor)

def test_create_athlete_instance():
    athlete = Athlete(name = 'Christine Jacoba Aaftink', sex = 'F', age = 21, height = 185, weight = 82)
    assert isinstance(athlete, Athlete)
    assert athlete.__dict__['name'] == 'Christine Jacoba Aaftink'

def test_results(build_results):
    results = build_results.results(cursor)
    medals = [result.medal for result in results]
    assert medals == [None, 'Silver']

def test_events(build_events):
    events = build_events.events(cursor)
    event_names = [event.event for event in events]
    assert event_names == ["Swimming Men's 100 metres Butterfly", "Swimming Men's 200 metres Butterfly"]

def test_names(build_athletes):
    results = Athlete.names(cursor)
    athlete_names = [athlete.__dict__['name'] for athlete in results]
    assert athlete_names == ['Michael Fred Phelps, II', 'Ronny Ackermann', 'Samir At Sad']

def test_find_athlete_by_name(build_athletes):
    results = [Athlete.find_athlete_by_name(cursor, athlete.name) for athlete in build_athletes]
    names = [result[0].__dict__['name'] for result in results]
    assert names == ['Michael Fred Phelps, II', 'Ronny Ackermann', 'Samir At Sad']

def test_find_athlete_by_id(build_athletes):
    result = Athlete.find_athlete_by_id(cursor, build_athletes[1].id) 
    id = result.__dict__['id']
    assert id == 702