from FootballMatch.Player import Player
from FootballMatch.Score import Score
from FootballMatch.Team import Team
from FootballMatch.GameAction.Shot import Shot

from App.EventDispatcher import EventDispatcher

import random

class Game:
    def __init__(self, homeTeam: Team, awayTeam: Team):
        self.__homeTeam = homeTeam
        self.__awayTeam = awayTeam
        
        # In the future this could be passed in when a Game instance is created
        # this would help with games that are played over two legs and have
        # aggregate scores
        self.__score = Score(0, 0)

        # TODO: inject this
        self.__eventDispatcher = EventDispatcher()

    def getScore(self) -> Score:
        return self.__score

    def getHomeTeam(self) -> Team:
        return self.__homeTeam

    def getAwayTeam(self) -> Team:
        return self.__awayTeam

    # TODO
    def shot(self, player: Player, timeInSeconds: int, onTarget: bool = False):
        shot = Shot(player, timeInSeconds, onTarget)
        self.__eventDispatcher.dispatchNow(shot)

    # TODO
    def save(self):
        pass

    # TODO
    def tackle(self):
        pass

    # TODO - pass is a reserved word in python... :(
    def passAttempt(self):
        pass

    # Not sure about the two pass methods yet, needs more thought...

    # TODO
    def passReceive(self):
        pass

    # TODO
    def interception(self):
        pass

    # TODO
    def deflection(self):
        pass

    def goal(self, scoringTeam: Team, scorer: Player, timeInSeconds: int):
        if self.__homeTeam == scoringTeam:
            self.__score.homeTeamScored()
        else:
            self.__score.awayTeamScored()
