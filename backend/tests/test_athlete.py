from backend.api.models import *
import pytest
from .test_db_utilities import *

@pytest.fixture
def athlete_results():
    pass

def test_create_athlete_instance():
    athlete = Athlete(name = 'Christine Jacoba Aaftink', sex = 'F', age = 21, height = 185, weight = 82)
    assert isinstance(athlete, Athlete)
    assert athlete.__dict__['name'] == 'Christine Jacoba Aaftink'

def test_athletes():
    pass