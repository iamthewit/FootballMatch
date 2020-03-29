from typing import Optional

from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from FootballMatch.GameAction.PassAttempt import PassAttempt
from FootballMatch.GameAction.Shot import Shot

from FootballMatch.GameAction.Rule.AbstractGameActionRule import AbstractGameActionRule


class DeflectionRule(AbstractGameActionRule):
    valid_previous_action_types = (
        PassAttempt,
        Shot
    )

    def __init__(self, game_action: AbstractGameAction, previous_game_action: Optional[AbstractGameAction]):
        super().__init__(game_action, previous_game_action)

    def check(self):
        # If type of previous action is not in the tuple of valid action types
        if not isinstance(self.previous_game_action, self.valid_previous_action_types):
            return False

        # if player who committed previous action is the same player that cause the deflection return false

        # if the time of the action is less than the time of the previous action
        # (this could be accounted for in the super class??)

        return True
