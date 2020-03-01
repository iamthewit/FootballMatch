import unittest

from Factory.PlayerFactory import PlayerFactory

from FootballMatch.Club import Club
from FootballMatch.Player import Player
from FootballMatch.Position.Defender import Defender

from pprint import pprint

class PlayerFactoryTest(unittest.TestCase):
    def setUp(self):
        self.factory = PlayerFactory()

    def test_createDefenderForClub(self):
        club = Club('Test Club')
        player = self.factory.createDefenderForClub(club)

        assert(isinstance(player, Player))
        assert(isinstance(player.position(), Defender))