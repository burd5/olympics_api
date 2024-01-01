import backend.api.models as models

class Country:
    __table__ = 'teams'
    attributes = ['id', 'team', 'noc']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                print(f'{key} not in {self.attributes}')
        for k, v in kwargs.items():
            setattr(self, k, v)
       
    def athletes(self, cursor):
        cursor.execute("""select distinct * from athletes where team = %s;""", (self.__dict__['team'],))
        records = cursor.fetchall()
        return models.build_from_records(models.Athlete, records)
    
    def medals(self, cursor):
        cursor.execute("""select team, 
                      SUM(CASE WHEN medal = 'Gold' THEN 1 else 0 end) as gold_medals,
                      SUM(CASE WHEN medal = 'Silver' THEN 1 else 0 end) as silver_medals,
                      SUM(CASE WHEN medal = 'Bronze' THEN 1 else 0 end) as bronze_medals
                      from results where team = %s group by 1;""", (self.__dict__['team'],))
        medals = cursor.fetchone()
        attributes = ['team', 'gold_medals', 'silver_medals', 'bronze_medals']
        medal_dict = dict(zip(attributes,medals))
        return medal_dict
    
    @classmethod
    def find_country_by_name(cls, cursor, name):
        cursor.execute("""select * from teams where team = INITCAP(%s);""", (name,))
        record = cursor.fetchone()
        return models.build_from_record(models.Country, record)
    
    @classmethod
    def all_names(cls, cursor):
        cursor.execute("""select distinct * from teams;""")
        records = cursor.fetchall()
        return models.build_from_records(models.Country, records)
    



    