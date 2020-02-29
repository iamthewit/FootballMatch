from pprint import pprint

from GameAction.AbstractGameAction import AbstractGameAction

from App.EventBus import EventBus

class EventDispatcher:
    def __init__(self):
        super().__init__()

    def dispatchNow(self, gameAction: AbstractGameAction):
        pprint(gameAction)
        eventBus = EventBus()
        eventBus.push(gameAction)