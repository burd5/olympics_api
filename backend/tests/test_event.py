from api.models.event import Event

def test_create_athlete_instance():
    attrs = ["Alpine Skiing Men's Downhill", 'Alpine Skiing']
    event = Event(attrs)

    assert isinstance(event, Event)