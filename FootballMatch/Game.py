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

import random

class Game:
    def __init__(self, homeTeam: Team, awayTeam: Team, score: Score, eventDispatcher: EventDispatcher):
        self.__homeTeam = homeTeam
        self.__awayTeam = awayTeam
        
        # In the future this could be passed in when a Game instance is created
        # this would help with games that are played over two legs and have
        # aggregate scores
        self.__score = score

        self.__eventDispatcher = eventDispatcher

    def getScore(self) -> Score:
        return self.__score

    def getHomeTeam(self) -> Team:
        return self.__homeTeam

    def getAwayTeam(self) -> Team:
        return self.__awayTeam

    def goal(self, scoringTeam: Team, scorer: Player, timeInSeconds: int):
        if self.__homeTeam == scoringTeam:
            self.__score.homeTeamScored()
        else:
            self.__score.awayTeamScored()

    # Game Actions
    
    def shot(self, player: Player, timeInSeconds: int, onTarget: bool = False) -> Shot:
        shot = Shot(player, timeInSeconds, onTarget)
        self.__eventDispatcher.dispatchNow(shot)

        return shot

    def save(self, player: Player, timeInSeconds: int) -> Save:
        # TODO: check that player position is GoalKeeper
        save = Save(player, timeInSeconds)
        self.__eventDispatcher.dispatchNow(save)

        return save

    def tackle(self, player: Player, timeInSeconds: int) -> Tackle:
        tackle = Tackle(player, timeInSeconds)
        self.__eventDispatcher.dispatchNow(tackle)

        return tackle

    def passAttempt(self, player: Player, timeInSeconds: int) -> PassAttempt:
        passAttempt = PassAttempt(player, timeInSeconds)
        self.__eventDispatcher.dispatchNow(passAttempt)

        return passAttempt

    def passReceive(self, player: Player, timeInSeconds: int) -> PassReceive:
        passReceive = PassReceive(player, timeInSeconds)
        self.__eventDispatcher.dispatchNow(passReceive)

        return passReceive

    def interception(self, player: Player, timeInSeconds: int) -> Interception:
        interception = Interception(player, timeInSeconds)
        self.__eventDispatcher.dispatchNow(interception)

        return interception

    def deflection(self, player: Player, timeInSeconds: int) -> Deflection:
        deflection = Deflection(player, timeInSeconds)
        self.__eventDispatcher.dispatchNow(deflection)

        return deflection

    def run(self, player: Player, timeInSeconds: int) -> Run:
        run = Run(player, timeInSeconds)
        self.__eventDispatcher.dispatchNow(run)

        return run