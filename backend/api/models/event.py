import backend.api.models as models

class Event:
    __table__ = 'events'
    attributes = ['event', 'sport']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.attributes:
                print(f'{key} not in {self.attributes}')
        for k, v in kwargs.items():
            setattr(self, k, v)

    # add filter for medal/year
    def results(self, cursor):
        pass

    # add filter for year/country
    def athletes(self, cursor):
        pass

    @classmethod
    def all_events(cls, cursor):
        pass

    