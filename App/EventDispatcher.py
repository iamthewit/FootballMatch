from GameAction.AbstractGameAction import AbstractGameAction
from App.EventBus import EventBus

class EventDispatcher:
    def __init__(self):
        super().__init__()

    def dispatchNow(self, gameAction: AbstractGameAction):
        eventBus = EventBus()
        eventBus.push(gameAction)