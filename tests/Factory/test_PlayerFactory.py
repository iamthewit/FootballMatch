import unittest

from Factory.PlayerFactory import PlayerFactory

from FootballMatch.Club import Club
from FootballMatch.Player import Player
from FootballMatch.Position.Defender import Defender
from FootballMatch.Position.Forward import Forward
from FootballMatch.Position.GoalKeeper import GoalKeeper
from FootballMatch.Position.Midfielder import Midfielder

from pprint import pprint

class PlayerFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PlayerFactory()

    def test_createDefenderForClub(self):
        club = Club('Test Club')
        player = self.factory.createDefenderForClub(club)

        assert(isinstance(player, Player))
        assert(isinstance(player.position(), Defender))

    def test_createForwardForClub(self):
        club = Club('Test Club')
        player = self.factory.createForwardForClub(club)

        assert(isinstance(player, Player))
        assert(isinstance(player.position(), Forward))

    def test_createGoalKeeperForClub(self):
        club = Club('Test Club')
        player = self.factory.createGoalKeeperForClub(club)

        assert(isinstance(player, Player))
        assert(isinstance(player.position(), GoalKeeper))

    def test_createMidfielderForClub(self):
        club = Club('Test Club')
        player = self.factory.createMidfielderForClub(club)

        assert(isinstance(player, Player))
        assert(isinstance(player.position(), Midfielder))