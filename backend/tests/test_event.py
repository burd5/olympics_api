from backend.api.models.event import Event
from backend.api.lib.db_utilities import *

def test_create_athlete_instance():
    attrs = ["Alpine Skiing Men's Downhill", 'Alpine Skiing']
    event = Event()

    assert isinstance(event, Event)