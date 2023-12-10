class Event:
    __table__ = 'olympics'
    columns = ['event', 'sport']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))