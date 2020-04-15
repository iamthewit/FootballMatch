from typing import Optional

from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from FootballMatch.GameAction.Deflection import Deflection
from FootballMatch.GameAction.Interception import Interception
from FootballMatch.GameAction.KickOff import KickOff
from FootballMatch.GameAction.PassReceive import PassReceive
from FootballMatch.GameAction.Rule.AbstractGameActionRule import AbstractGameActionRule
from FootballMatch.GameAction.Run import Run
from FootballMatch.GameAction.Save import Save
from FootballMatch.GameAction.Tackle import Tackle


class PassAttemptRule(AbstractGameActionRule):
    valid_previous_action_types = (
        Deflection,
        Interception,
        KickOff,
        PassReceive,
        Run,
        Save,
        Tackle,
    )

    valid_next_action_types = (
        Deflection,
        Interception,
        PassReceive,
    )

    def __init__(self, game_action: AbstractGameAction, previous_game_action: Optional[AbstractGameAction]):
        super().__init__(game_action, previous_game_action)

    def check(self):
        # If type of previous action is not in the tuple of valid action types
        if not isinstance(self.previous_game_action, self.valid_previous_action_types):
            return False
            # TODO: this could be accounted for in the super class maybe?

        # If the time of the action is less than the time of the previous action
        if self.game_action.time_in_seconds < self.previous_game_action.time_in_seconds:
            return False
            # TODO: this could be accounted for in the super class maybe?
            # depends if it's valid for all rules?

        return True
