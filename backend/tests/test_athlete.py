from api.models.athlete import *

def test_create_athlete_instance():
    attrs = [5, 'Christine Jacoba Aaftink', 'F',  21, 185, 82]
    athlete = Athlete(attrs)

    assert isinstance(athlete, Athlete)
