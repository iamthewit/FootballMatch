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

from FootballMatch.GameAction.Deflection import Deflection
from FootballMatch.GameAction.Interception import Interception
from FootballMatch.GameAction.PassAttempt import PassAttempt
from FootballMatch.GameAction.PassReceive import PassReceive
from FootballMatch.GameAction.Run import Run
from FootballMatch.GameAction.Save import Save
from FootballMatch.GameAction.Shot import Shot
from FootballMatch.GameAction.Tackle import Tackle

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
        shot = self.game.shot(self.homePlayer, 10, True)

        self.eventDispatcher.dispatchNow.assert_called_once()
        assert(isinstance(shot, Shot))
    
    def test_save(self):
        save = self.game.save(self.homePlayer, 10)

        self.eventDispatcher.dispatchNow.assert_called_once()
        assert(isinstance(save, Save))

    def test_tackle(self):
        tackle = self.game.tackle(self.homePlayer, 10)

        self.eventDispatcher.dispatchNow.assert_called_once()
        assert(isinstance(tackle, Tackle))
    
    def test_passAttempt(self):
        passAttempt = self.game.passAttempt(self.homePlayer, 10)

        self.eventDispatcher.dispatchNow.assert_called_once()
        assert(isinstance(passAttempt, PassAttempt))

    def test_passReceive(self):
        passReceive = self.game.passReceive(self.homePlayer, 10)

        self.eventDispatcher.dispatchNow.assert_called_once()
        assert(isinstance(passReceive, PassReceive))

    def test_interception(self):
        interception = self.game.interception(self.homePlayer, 10)

        self.eventDispatcher.dispatchNow.assert_called_once()
        assert(isinstance(interception, Interception))

    def test_deflection(self):
        deflection = self.game.deflection(self.homePlayer, 10)

        self.eventDispatcher.dispatchNow.assert_called_once()
        assert(isinstance(deflection, Deflection))

    def test_run(self):
        run = self.game.run(self.homePlayer, 10)

        self.eventDispatcher.dispatchNow.assert_called_once()
        assert(isinstance(run, Run))