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

    def results(self, cursor):
        cursor.execute("""select * from results where athlete_name = %s;""", (self.__dict__['name'],))
        records = cursor.fetchall()
        return models.build_from_records(models.Result, records)
    
    def events(self):
        pass

    @classmethod
    def names(cls):
        pass