class Medal:
    __table__ = 'olympics'
    columns = ['medal', 'games', 'event', 'name', 'team']

    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))