import psycopg2
import json


class Athlete:
    __table__ = 'olympics'
    columns = ['id', 'name', 'sex', 'age', 'height', 'weight', 'team', 'games', 'medal']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    # def find_medals_won(self):
    #     conn = psycopg2.connect(database=DATABASE, user=USER)
    #     cursor = conn.cursor()
    #     cursor.execute("""select distinct name, games,
    #                       SUM(CASE WHEN medal = 'Gold' THEN 1 else 0 end) as gold_medals,
    #                       SUM(CASE WHEN medal = 'Silver' THEN 1 else 0 end) as silver_medals,
    #                       SUM(CASE WHEN medal = 'Bronze' THEN 1 else 0 end) as bronze_medals
    #                       from olympics where name = %s group by name, games;""", (self.__dict__['name'],))
    #     columns = ['name', 'games', 'gold', 'silver', 'bronze']
    #     medals = cursor.fetchall()
    #     return [dict(zip(columns, medal)) for medal in medals][0]