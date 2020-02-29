from GameAction.AbstractGameAction import AbstractGameAction
from App.LogEventToFile import LogEventToFile

from pprint import pprint

class EventBus:
    listeners = {
        'AbstractGameAction': 'LogEventToFile'
    }

    def __init__(self):
        super().__init__()

    def push(self, event: AbstractGameAction):
        for key, value in self.listeners:
            pprint(key, value)
            # if isinstance(event, key):
            #     listener = getattr(value, value)
            #     listener.handle()