from backend.api.models import *
import pytest
from backend.api.lib.db_utilities import *

@pytest.fixture()
def build_country_athletes():
    drop_all_tables(conn, cursor)
    cambodia = Country(team='Cambodia', noc='CAM')
    save(cambodia, conn, cursor)
    athlete1 = Athlete(id = 40068, name = 'Chhay-Kheng Nhem', sex = 'M', age = 25.0, height =  171.0, weight = 70.0, team = 'Cambodia')
    save(athlete1, conn, cursor)
    athlete2 = Athlete(id = 93851, name = 'Hem Bunting', sex = 'M', age = 22.0, height = 167.0, weight = 63.0, team = 'Cambodia')
    save(athlete2, conn, cursor)
    yield cambodia
    drop_all_tables(conn, cursor)

def test_create_country_instance():
    country = Country(team='Germany', noc='GER')
    assert isinstance(country, Country)
    assert country.__dict__['team'] == 'Germany' 

def test_country_athletes(build_country_athletes):
    athletes = build_country_athletes.athletes(cursor)
    athlete_names = [athlete.name for athlete in athletes]
    assert athlete_names == ['Chhay-Kheng Nhem', 'Hem Bunting']