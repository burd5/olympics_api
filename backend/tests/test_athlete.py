from api.models.athlete import Athlete

def test_create_athlete_instance():
    attrs = ['Christine Jacoba Aaftink', 'F',  21, 185, 82]
    athlete = Athlete(attrs)

    assert isinstance(athlete, Athlete)


