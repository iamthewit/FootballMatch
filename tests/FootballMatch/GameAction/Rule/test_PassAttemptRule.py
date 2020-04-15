import unittest

from FootballMatch.Club import Club
from FootballMatch.GameAction.Interception import Interception
from FootballMatch.GameAction.PassReceive import PassReceive
from FootballMatch.GameAction.Rule.PassAttemptRule import PassAttemptRule
from FootballMatch.GameAction.Run import Run
from FootballMatch.GameAction.Save import Save
from FootballMatch.GameAction.Tackle import Tackle
from FootballMatch.Player import Player

from FootballMatch.GameAction.Deflection import Deflection
from FootballMatch.GameAction.KickOff import KickOff
from FootballMatch.GameAction.PassAttempt import PassAttempt
from FootballMatch.GameAction.Shot import Shot

from FootballMatch.GameAction.Rule.DeflectionRule import DeflectionRule

from FootballMatch.Position.Forward import Forward


class PassAttemptRuleTest(unittest.TestCase):
    valid_previous_action_types = (
        Deflection,
        Interception,
        KickOff,
        PassReceive,
        Run,
        Save,
        Tackle,
    )

    invalid_previous_actions = (
        PassAttempt,
    )

    def setUp(self) -> None:
        self.previous_club = Club("Previous club Name")
        self.previous_player = Player(9, "Previous Player Name", Forward(), self.previous_club)

        self.club = Club("Club Name")
        self.player = Player(9, "Player Name", Forward(), self.club)

    def test_it_returns_false_for_invalid_previous_actions(self):
        for invalid_previous_action in self.invalid_previous_actions:
            previous_game_action = invalid_previous_action(self.previous_player, 0)
            game_action = PassAttempt(self.player, 0)

            rule = PassAttemptRule(game_action, previous_game_action)

            assert(rule.check() is False)

    def test_it_returns_false_if_current_action_occurs_before_previous_action(self):
        previous_game_action = PassReceive(self.previous_player, 10)
        game_action = PassAttempt(self.player, 0)

        rule = PassAttemptRule(game_action, previous_game_action)

        assert (rule.check() is False)

    def test_it_returns_true_for_valid_previous_actions(self):
        for valid_previous_action_type in self.valid_previous_action_types:
            valid_previous_action = valid_previous_action_type(self.previous_player, 0)
            action = PassAttempt(self.player, 0)

            rule = PassAttemptRule(action, valid_previous_action)

            assert (rule.check() is True)
