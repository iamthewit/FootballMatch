import unittest

from FootballMatch.Club import Club
from FootballMatch.Player import Player

from FootballMatch.GameAction.Deflection import Deflection
from FootballMatch.GameAction.KickOff import KickOff
from FootballMatch.GameAction.PassAttempt import PassAttempt
from FootballMatch.GameAction.Shot import Shot

from FootballMatch.GameAction.Rule.DeflectionRule import DeflectionRule

from FootballMatch.Position.Forward import Forward


class DeflectionRuleTest(unittest.TestCase):
    valid_previous_action_types = (
        PassAttempt,
        Shot
    )

    def setUp(self) -> None:
        self.previous_club = Club("Name")
        self.previous_player = Player(9, "Name", Forward(), self.previous_club)

        self.club = Club("Name")
        self.player = Player(9, "Name", Forward(), club)

    def test_it_returns_true_for_valid_previous_actions(self):
        # TODO: refactor test to iterate over valid_previous_action_types
        previous_game_action = PassAttempt(self.previous_player, 0)
        game_action = Deflection(self.player, 0)

        rule = DeflectionRule(game_action, previous_game_action)

        assert(rule.check())

    def test_it_returns_false_for_invalid_previous_actions(self):
        previous_game_action = KickOff(self.previous_player, 0)
        game_action = Deflection(self.player, 0)

        rule = DeflectionRule(game_action, previous_game_action)

        assert(rule.check() is False)

    def test_it_returns_false_if_previous_action_player_is_same_as_current_action_player(self):
        previous_game_action = PassAttempt(self.previous_player, 0)
        game_action = Deflection(self.previous_player, 0)

        rule = DeflectionRule(game_action, previous_game_action)

        assert(rule.check() is False)

    def test_it_returns_false_if_current_action_occurs_before_previous_action(self):
        previous_game_action = PassAttempt(self.previous_player, 10)
        game_action = Deflection(self.player, 0)

        rule = DeflectionRule(game_action, previous_game_action)

        assert (rule.check() is False)
