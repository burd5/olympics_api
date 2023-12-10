from flask import Flask, jsonify
import json
import psycopg2
from .models.country import Country
from .models.athlete import Athlete
from .models.event import Event
from .models.medal import Medal
from .models.record import Record

def create_app(database,user):

    app = Flask(__name__)

    @app.route('/')
    def all_records():
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select * from olympics;""")
        records = cursor.fetchall()
        return json.dumps([Record(record).__dict__ for record in records])
    
    @app.route('/countries')
    def countries():
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select distinct team, noc from olympics order by team asc;""")
        countries = cursor.fetchall()
        return json.dumps([Country(country).__dict__ for country in countries])
    
    @app.route('/countries/<name>')
    def country(name):
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select distinct team, noc, array_agg(distinct event) from olympics where team ILIKE '%%'||%s||'%%' group by team, noc order by team asc;""", (name,))
        countries = cursor.fetchall()
        return json.dumps([Country(country).__dict__ for country in countries])
    
    @app.route('/athletes')
    def athletes():
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select name, sex, age, height, weight, team from olympics;""")
        athletes = cursor.fetchall()
        return json.dumps([Athlete(athlete).__dict__ for athlete in athletes])
    
    @app.route('/athletes/<id>')
    def athlete(id):
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select distinct id, name, sex, age, height, weight, team from olympics where id = %s;""", (id,))
        athletes = cursor.fetchall()
        return json.dumps([Athlete(athlete).__dict__ for athlete in athletes])
    
    @app.route('/events')
    def sports():
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select distinct event, sport from olympics order by event asc;""")
        events = cursor.fetchall()
        return json.dumps([Event(event).__dict__ for event in events])
    
    @app.route('/events/<sport>')
    def events_per_sport(sport):
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select distinct event, sport from olympics where sport ILIKE '%%'||%s||'%%'  order by event asc;""", (sport,))
        events = cursor.fetchall()
        return json.dumps([Event(event).__dict__ for event in events])


    @app.route('/medals')
    def medals():
        conn = psycopg2.connect(database=database, user=user)
        cursor = conn.cursor()
        cursor.execute("""select medal, games, event, name, team from olympics where medal IS NOT NULL order by games, medal;""")
        medals = cursor.fetchall()
        return json.dumps([Medal(medal).__dict__ for medal in medals])
    
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
