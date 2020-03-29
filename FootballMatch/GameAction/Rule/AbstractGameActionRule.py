from abc import ABC
from typing import Optional

from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction


class AbstractGameActionRule(ABC):
    def __init__(self, game_action: AbstractGameAction, previous_game_action: Optional[AbstractGameAction]):
        self.game_action = game_action
        self.previous_game_action = previous_game_action

    def check(self) -> bool:
        pass
