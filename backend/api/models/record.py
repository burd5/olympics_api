class Record:
    __table__ = 'olympics'
    columns = ['id', 'name', 'sex', 'age', 'height', 'weight', 'team', 'noc', 'games', 'year', 'season', 'city', 'sport', 'event', 'medal']

    def  __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))