from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from App.EventBus import EventBus

class EventDispatcher:
    def __init__(self, eventBus: EventBus):
        super().__init__()
        self.__eventBus = eventBus

    def dispatchNow(self, gameAction: AbstractGameAction):
        self.__eventBus.push(gameAction)