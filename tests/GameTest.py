import unittest
from Club import Club
from Game import Game
from Forward import Forward
from Player import Player
from Team import Team

class GameTest(unittest.TestCase):
    def setUp(self):
        self.homeClub = Club('Home')
        self.homeTeam = Team(self.homeClub)
        self.homePlayer = Player(9, "Cross", Forward(), self.homeClub)

        self.awayClub = Club('Away')
        self.awayTeam = Team(self.awayClub, False)

        self.game = Game(self.homeTeam, self.awayTeam)

    def test_goal(self):
        self.game.goal(self.homeTeam, self.homePlayer, 1)
        assert(1 == self.game.score.homeTeamScore)