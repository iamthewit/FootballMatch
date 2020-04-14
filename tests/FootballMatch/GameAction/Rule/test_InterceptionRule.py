import unittest

from FootballMatch.Club import Club
from FootballMatch.GameAction.Deflection import Deflection
from FootballMatch.GameAction.Interception import Interception
from FootballMatch.GameAction.KickOff import KickOff
from FootballMatch.GameAction.PassAttempt import PassAttempt
from FootballMatch.GameAction.PassReceive import PassReceive
from FootballMatch.GameAction.Rule.InterceptionRule import InterceptionRule
from FootballMatch.GameAction.Run import Run
from FootballMatch.GameAction.Save import Save
from FootballMatch.GameAction.Shot import Shot
from FootballMatch.GameAction.Tackle import Tackle
from FootballMatch.Player import Player
from FootballMatch.Position.Forward import Forward


class InterceptionRuleTest(unittest.TestCase):
    valid_previous_action_types = (
        Deflection,
        PassAttempt,
        Shot
    )

    invalid_previous_action_types = (
        Interception,
        KickOff,
        PassReceive,
        Run,
        Save,
        Tackle
    )

    def setUp(self) -> None:
        self.previous_club = Club("Previous Club Name")
        self.previous_player = Player(9, 'Previous Player Name', Forward(), self.previous_club)

        self.club = Club('Club Name')
        self.player = Player(9, 'Player Name', Forward(), self.club)

    def test_it_returns_false_if_previous_action_is_invalid(self):
        for invalid_previous_action_type in self.invalid_previous_action_types:
            invalid_previous_action = invalid_previous_action_type(self.previous_player, 0)
            action = Interception(self.player, 0)

            rule = InterceptionRule(action, invalid_previous_action)

            assert(rule.check() is False)

    def test_it_returns_false_if_previous_action_player_is_same_as_current_action_player(self):
        previous_game_action = Deflection(self.player, 0)
        game_action = Interception(self.player, 0)

        rule = InterceptionRule(game_action, previous_game_action)

        assert(rule.check() is False)

    def test_it_returns_true_for_valid_previous_actions(self):
        for valid_previous_action_type in self.valid_previous_action_types:
            valid_previous_action = valid_previous_action_type(self.previous_player, 0)
            action = Interception(self.player, 0)

            rule = InterceptionRule(action, valid_previous_action)

            assert(rule.check() is True)
