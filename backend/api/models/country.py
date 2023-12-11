import psycopg2
class Country:
    __table__ = 'olympics'
    columns = ['team', 'noc', 'events']

    def __init__(self, values, database, user):
        self.__dict__ = dict(zip(self.columns, values))
        self.database = database
        self.user = user

    def find_all_athletes_for_country(self):
        conn = psycopg2.connect(database=self.database, user=self.user)
        cursor = conn.cursor()
        statement = """select distinct id, name from olympics where team = %s;"""
        cursor.execute(statement, (self.__dict__['team'],))
        athletes = cursor.fetchall()
        attrs = ['id', 'name']
        return [dict(zip(attrs, athlete)) for athlete in athletes]


    