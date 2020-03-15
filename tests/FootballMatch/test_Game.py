import unittest
from unittest.mock import MagicMock
from unittest.mock import Mock
from pprint import pprint

from FootballMatch.Club import Club
from FootballMatch.Game import Game
from FootballMatch.Position.Forward import Forward
from FootballMatch.Player import Player
from FootballMatch.Score import Score
from FootballMatch.Team import Team

from App.EventDispatcher import EventDispatcher
from App.EventBus import EventBus

class GameTest(unittest.TestCase):
    def setUp(self):
        self.homeClub = Club('Home')
        self.homeTeam = Team(self.homeClub)
        self.homePlayer = Player(9, "Cross", Forward(), self.homeClub)

        self.awayClub = Club('Away')
        self.awayTeam = Team(self.awayClub, False)

        self.score = Score()
        self.eventDispatcher = MagicMock()

        self.game = Game(self.homeTeam, self.awayTeam, self.score, self.eventDispatcher)

    def test_goal(self):
        self.game.goal(self.homeTeam, self.homePlayer, 1)
        
        assert(1 == self.game.getScore().getHomeTeamScore())

    def test_score(self):
        assert(isinstance(self.game.getScore(), Score))

    def test_shot(self):
        self.game.shot(self.homePlayer, 10, True)
        self.eventDispatcher.dispatchNow.assert_called_once()