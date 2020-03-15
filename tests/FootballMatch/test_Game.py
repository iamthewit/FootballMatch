import unittest
from pprint import pprint

from FootballMatch.Club import Club
from FootballMatch.Game import Game
from FootballMatch.Position.Forward import Forward
from FootballMatch.Player import Player
from FootballMatch.Score import Score
from FootballMatch.Team import Team

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
        
        assert(1 == self.game.getScore().getHomeTeamScore())

    def test_score(self):
        assert(isinstance(self.game.getScore(), Score))

    def test_shot(self):
        self.game.shot(self.homePlayer, 10, True)
        # TODO: in order to assert the event was dispatched
        # we need to allow the event dispatcher to be injected
        # into the game class so that we can pass a mocked event
        # dispatcher in in the test setup