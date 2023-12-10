class Athlete:
    __table__ = 'olympics'
    columns = ['name', 'sex', 'age', 'height', 'weight', 'team']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))