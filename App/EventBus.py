from GameAction.AbstractGameAction import AbstractGameAction
from App.LogEventToFile import LogEventToFile

class EventBus:
    listeners = {
        AbstractGameAction: LogEventToFile
    }

    def __init__(self):
        super().__init__()

    def push(self, event: AbstractGameAction):
        for key, value in self.listeners.items():
            if isinstance(event, key):
                value().handle(event)