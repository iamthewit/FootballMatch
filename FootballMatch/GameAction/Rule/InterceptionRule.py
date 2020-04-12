from typing import Optional

from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from FootballMatch.GameAction.PassAttempt import PassAttempt
from FootballMatch.GameAction.Run import Run
from FootballMatch.GameAction.Save import Save
from FootballMatch.GameAction.Shot import Shot

from FootballMatch.GameAction.Rule.AbstractGameActionRule import AbstractGameActionRule


class InterceptionRule(AbstractGameActionRule):
    valid_previous_action_types = (
        PassAttempt,
        Shot
    )

    valid_next_action_types = (
        PassAttempt,
        Run,
        Shot
    )

    def __init__(self, game_action: AbstractGameAction, previous_game_action: Optional[AbstractGameAction]):
        super().__init__(game_action, previous_game_action)

    def check(self):
        # If type of previous action is not in the tuple of valid action types
        if not isinstance(self.previous_game_action, self.valid_previous_action_types):
            return False

        # If player who committed previous action is the same player that caused the interception
        if self.game_action.player.__eq__(self.previous_game_action.player):
            return False

        # If the time of the action is less than the time of the previous action
        if self.game_action.time_in_seconds < self.previous_game_action.time_in_seconds:
            return False

        return True
