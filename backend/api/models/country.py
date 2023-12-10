class Country:
    __table__ = 'olympics'
    columns = ['team', 'noc']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))