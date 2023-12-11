import psycopg2
from settings import DATABASE, USER
class Country:
    __table__ = 'olympics'
    columns = ['team', 'noc']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
       

    def find_all_athletes_for_country(self):
        conn = psycopg2.connect(database=DATABASE, user=USER)
        cursor = conn.cursor()
        statement = """select distinct id, name from olympics where team = %s;"""
        cursor.execute(statement, (self.__dict__['team'],))
        athletes = cursor.fetchall()
        attrs = ['id', 'name']
        return [dict(zip(attrs, athlete)) for athlete in athletes]


    