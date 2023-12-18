import backend.api.models as models

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
        return models.build_from_records(models.Result, records)
    
    def events(self, cursor):
        cursor.execute("""select e.event, e.sport from results r
                          join events e on r.event = e.event 
                          where r.athlete_id = %s;""", (self.__dict__['id'],))
        records = cursor.fetchall()
        return models.build_from_records(models.Event, records)
    
    @classmethod
    def find_athlete_by_name(cls, cursor, name):
        cursor.execute("""select * from athletes where name ILIKE '%%'||%s||'%%';""", (name,))
        records = cursor.fetchall()
        return models.build_from_records(models.Athlete, records)
    
    @classmethod
    def find_athlete_by_id(cls, cursor, id):
        cursor.execute("""select * from athletes where id = %s;""", (id,))
        record = cursor.fetchone()
        return models.build_from_record(models.Athlete, record)

    @classmethod
    def names(cls, cursor):
        cursor.execute("""select * from athletes;""")
        records = cursor.fetchall()
        return models.build_from_records(models.Athlete, records)