import backend.api.models as models

class Result:
    __table__ = 'results'
    attributes = ['id', 'athlete_id', 'team', 'games', 'event', 'medal']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                print(f'{key} not in {self.attributes}')
        for k, v in kwargs.items():
            setattr(self, k, v)