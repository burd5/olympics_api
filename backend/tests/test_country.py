from backend.api.models import *
import pytest
from backend.api.lib.db_utilities import *

@pytest.fixture()
def build_country_athletes():
    drop_all_tables(test_conn, test_cursor)
    cambodia = Country(team='Cambodia', noc='CAM')
    save(cambodia, test_conn, test_cursor)
    athlete1 = Athlete(id = 40068, name = 'Chhay-Kheng Nhem', sex = 'M', age = 25.0, height =  171.0, weight = 70.0, team = 'Cambodia')
    save(athlete1, test_conn, test_cursor)
    athlete2 = Athlete(id = 93851, name = 'Hem Bunting', sex = 'M', age = 22.0, height = 167.0, weight = 63.0, team = 'Cambodia')
    save(athlete2, test_conn, test_cursor)
    yield cambodia
    drop_all_tables(test_conn, test_cursor)

@pytest.fixture()
def build_countries():
    drop_all_tables(test_conn, test_cursor)
    cambodia = Country(team='Cambodia', noc='CAM')
    save(cambodia, test_conn, test_cursor)
    usa = Country(team='United States', noc='USA')
    save(usa, test_conn, test_cursor)
    china = Country(team='China', noc='CHN')
    save(china, test_conn, test_cursor)
    yield [cambodia,usa,china]
    drop_all_tables(test_conn, test_cursor)

def test_create_country_instance():
    country = Country(team='Germany', noc='GER')
    assert isinstance(country, Country)
    assert country.__dict__['team'] == 'Germany' 

def test_country_athletes(build_country_athletes):
    athletes = build_country_athletes.athletes(cursor)
    athlete_names = [athlete.name for athlete in athletes]
    assert athlete_names == ['Chhay-Kheng Nhem', 'Hem Bunting']

def test_find_country_by_name(build_countries):
    country = Country.find_country_by_name(cursor, 'China')
    assert country.noc == 'CHN' #type:ignore

def test_all_names(build_countries):
    countries = Country.all_names(cursor)
    country_names = [country.team for country in countries] # type: ignore
    assert country_names == sorted(['Cambodia', 'United States', 'China'], reverse = True)