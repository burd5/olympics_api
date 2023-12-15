import backend.api.models as models

class Game:
    __table__ = 'games'
    attributes = ['games', 'year', 'season', 'city']


def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                print(f'{key} not in {self.attributes}')
        for k, v in kwargs.items():
            setattr(self, k, v)