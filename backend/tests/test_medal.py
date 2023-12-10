from api.models.medal import Medal

def test_create_athlete_instance():
    attrs = ["Gymanastics Men's Rings", '1896 Summer', 'Gold', 'Ellery Harding Clark', 'United States']
    medal = Medal(attrs)

    assert isinstance(medal, Medal)