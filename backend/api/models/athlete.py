import backend.api.models as models
import json

class Athlete:
    __table__ = 'athletes'
    attributes = ['id', 'name', 'sex', 'age', 'height', 'weight', 'team']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                print(f'{key} not in {self.attributes}')
        for k, v in kwargs.items():
            setattr(self, k, v)

    def results(self, cursor) -> list[object]:
        cursor.execute("""select * from results where athlete_id = %s;""", (self.__dict__['id'],))
        records = cursor.fetchall()
        return models.build_from_records(models.Result, records) # type: ignore
    
    def events(self, cursor):
        cursor.execute("""select e.event, e.sport from results r
                          join events e on r.event = e.event 
                          where r.athlete_id = %s;""", (self.__dict__['id'],))
        records = cursor.fetchall()
        return models.build_from_records(models.Event, records)
    
    def medals(self, cursor):
        cursor.execute("""select athlete_id, 
                      SUM(CASE WHEN medal = 'Gold' THEN 1 else 0 end) as gold_medals,
                      SUM(CASE WHEN medal = 'Silver' THEN 1 else 0 end) as silver_medals,
                      SUM(CASE WHEN medal = 'Bronze' THEN 1 else 0 end) as bronze_medals
                      from results where athlete_id = %s group by 1;""", (self.__dict__['id'],))
        medals = cursor.fetchone()
        attributes = ['id', 'gold_medals', 'silver_medals', 'bronze_medals']
        medal_dict = dict(zip(attributes,medals))
        medal_dict['name'] = self.__dict__['name']
        return medal_dict
    
    def games(self, cursor):
        cursor.execute("""select distinct g.* from games g
                          join results r on r.games = g.games
                          where r.athlete_id = %s order by year asc;""", (self.__dict__['id'],))
        games = cursor.fetchall()
        return models.build_from_records(models.Game, games)
    
    @classmethod
    def find_athlete_by_name(cls, cursor, name):
        cursor.execute("""select * from athletes where name ILIKE '%%'||%s||'%%';""", (name,))
        athletes = cursor.fetchall()
        return models.build_from_records(models.Athlete, athletes)
    
    @classmethod
    def find_athlete_by_id(cls, cursor, id):
        cursor.execute("""select * from athletes where id = %s;""", (id,))
        athlete = cursor.fetchone()
        return models.build_from_record(models.Athlete, athlete)

    @classmethod
    def names(cls, cursor):
        cursor.execute("""select * from athletes;""")
        athletes = cursor.fetchall()
        return models.build_from_records(models.Athlete, athletes)