from Player import Player
from Score import Score
from Team import Team

class Game:
    def __init__(self, homeTeam: Team, awayTeam: Team):
        self.__homeTeam = homeTeam
        self.__awayTeam = awayTeam
        
        # In the future this could be passed in when a Game instance is created
        # this would help with games that are played over two legs and have
        # aggregate scores
        self.__score = Score(0, 0)

    def getScore(self) -> Score:
        return self.__score

    def getHomeTeam(self) -> Team:
        return self.__homeTeam

    def getAwayTeam(self) -> Team:
        return self.__awayTeam

    # TODO
    def shot(self):
        pass

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
