from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from App.EventBus import EventBus


class EventDispatcher:
    def __init__(self, event_bus: EventBus):
        super().__init__()
        self.__event_bus = event_bus

    def dispatch_now(self, game_action: AbstractGameAction):
        self.__event_bus.push(game_action)
