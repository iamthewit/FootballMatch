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

        # If player who committed previous action is the same player that caused the deflection
        if self.game_action.player.__eq__(self.previous_game_action.player):
            return False

        # If the time of the action is less than the time of the previous action
        if self.game_action.time_in_seconds < self.previous_game_action.time_in_seconds:
            return False
            # TODO: this could be accounted for in the super class maybe?
            # depends if it's valid for all rules?

        return True
