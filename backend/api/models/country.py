import backend.api.models as models

class Country:
    __table__ = 'teams'
    attributes = ['team', 'noc']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                print(f'{key} not in {self.attributes}')
        for k, v in kwargs.items():
            setattr(self, k, v)
       
    def athletes(self, cursor):
        statement = """select * from athletes where team = %s;"""
        cursor.execute(statement, (self.__dict__['team'],))
        records = cursor.fetchall()
        return [models.build_from_record(models.Athlete, record) for record in records]


    