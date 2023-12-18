from flask import Flask
import json
import psycopg2
from backend.api.models import *

def create_app(database,user, password):

    app = Flask(__name__)

    app.config.from_mapping(
        DATABASE = database,
        DB_USER = user,
        DB_PASSWORD = password
    )

    conn = psycopg2.connect(database=database, user=user, password=password)
    cursor = conn.cursor()

    # Render HTML template for home page 
    # @app.route('/')
    # def all_records():
    #     conn = psycopg2.connect(database=database, user=user)
    #     cursor = conn.cursor()
    #     cursor.execute("""select * from olympics;""")
    #     records = cursor.fetchall()
    #     return records
    
    @app.route('/countries')
    def countries():
        # calls @classmethod names from Athlete to return all matching Athlete instances
        return json.dumps([country.__dict__ for country in Country.all_names(cursor)])
    
    @app.route('/countries/<name>')
    def country(name):
        # calls @classmethod names from Country to return all matching Country instances
        return Country.find_country_by_name(cursor, name).__dict__
    
    @app.route('/countries/<name>/athletes')
    def country_athletes(name):
        country = Country.find_country_by_name(cursor, name)
        assert country is not None
        results = country.athletes(cursor) 
        return json.dumps([result.__dict__ for result in results])
    
    # countries_events = use array_agg(distinct events)
    @app.route('/athletes')
    def athletes():
        # calls @classmethod names from Athlete to return all matching Athlete instances
        return json.dumps([athlete.__dict__ for athlete in Athlete.names(cursor)])
    
    @app.route('/athletes/<name>')
    def athlete(name):
        # calls @classmethod find_athlete_by_name from Athlete to return all athletes with similar name
        return json.dumps([athlete.__dict__ for athlete in Athlete.find_athlete_by_name(cursor, name)])
    
    @app.route('/athletes/<id>/results')
    def athlete_results(id:int) -> list[dict]:
        athlete = Athlete.find_athlete_by_id(cursor, id)
        assert athlete is not None
        results = athlete.results(cursor) 
        return [result.__dict__ for result in results]
    
    @app.route('/athletes/<id>/events')
    def athlete_events(id:int) -> list[dict]:
        athlete = Athlete.find_athlete_by_id(cursor, id)
        assert athlete is not None
        results = athlete.events(cursor)
        return [result.__dict__ for result in results]
    
    # @app.route('/athletes/<id>/medals')
    # def athlete_medals(id):
    #     conn = psycopg2.connect(database=database, user=user)
    #     cursor = conn.cursor()
    #     cursor.execute("""select id, name, games,
    #                       SUM(CASE WHEN medal = 'Gold' THEN 1 else 0 end) as gold_medals,
    #                       SUM(CASE WHEN medal = 'Silver' THEN 1 else 0 end) as silver_medals,
    #                       SUM(CASE WHEN medal = 'Bronze' THEN 1 else 0 end) as bronze_medals
    #                       from olympics where id = %s group by id, name, games;""", (id,))
    #     columns = ['id', 'name', 'games', 'gold', 'silver', 'bronze']
    #     medals = cursor.fetchall()
    #     return json.dumps([dict(zip(columns, medal)) for medal in medals])
        
    
    @app.route('/events')
    def sports():
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select distinct event, sport from olympics order by event asc;""")
        events = cursor.fetchall()
        return json.dumps([build_from_record(Event, event).__dict__ for event in events])
    
    @app.route('/events/<sport>')
    def events_per_sport(sport):
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select distinct event, sport from olympics where sport ILIKE '%%'||%s||'%%'  order by event asc;""", (sport,))
        events = cursor.fetchall()
        return json.dumps([build_from_record(Event, event).__dict__ for event in events])


    @app.route('/results')
    def medals():
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select * from results;""")
        results = cursor.fetchall()
        return json.dumps([build_from_record(Result, result).__dict__ for result in results])
    
    
    @app.route('/medals/<country>')
    def medal_count_per_country(country):
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select team,
                          SUM(CASE WHEN medal = 'Gold' THEN 1 else 0 end) as gold_medals,
                          SUM(CASE WHEN medal = 'Silver' THEN 1 else 0 end) as silver_medals,
                          SUM(CASE WHEN medal = 'Bronze' THEN 1 else 0 end) as bronze_medals
                          from olympics where team ILIKE '%%'||%s||'%%' group by team;""", (country,))
        countries = cursor.fetchall()
        columns = ['team', 'gold', 'silver', 'bronze']
        return json.dumps([dict(zip(columns, country)) for country in countries])
    
    return app
