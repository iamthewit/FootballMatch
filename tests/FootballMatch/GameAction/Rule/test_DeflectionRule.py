import unittest

from FootballMatch.Club import Club
from FootballMatch.Player import Player

from FootballMatch.GameAction.Deflection import Deflection
from FootballMatch.GameAction.PassAttempt import PassAttempt
from FootballMatch.GameAction.Shot import Shot

from FootballMatch.GameAction.Rule.DeflectionRule import DeflectionRule

from FootballMatch.Position.Forward import Forward


class DeflectionRuleTest(unittest.TestCase):
    valid_previous_action_types = (
        PassAttempt,
        Shot
    )

    def test_it_returns_true_for_valid_previous_actions(self):
        previous_club = Club("Name")
        previous_player = Player(9, "Name", Forward(), previous_club)
        previous_game_action = PassAttempt(previous_player, 0)

        club = Club("Name")
        player = Player(9, "Name", Forward(), club)
        game_action = Deflection(player, 0)

        rule = DeflectionRule(game_action, previous_game_action)

        assert(rule.check())

        # TODO: refactor test to iterate over valid_previous_action_types
