from api.models.country import Country

def test_create_athlete_instance():
    attrs = ['GER', 'Germany/United States']
    country = Country(attrs)

    assert isinstance(country, Country)