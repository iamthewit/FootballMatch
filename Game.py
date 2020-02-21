from Player import Player
from Score import Score
from Team import Team

class Game:

    def __init__(self, homeTeam: Team, awayTeam: Team):
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam
        # in the future this could be passed in when a Game instance is created
        # this would help with games that are played over two legs and have 
        # aggregate scores
        self.score = Score(0, 0)
    
    def getScore(self) -> Score:
        return self.score

    def getHomeTeam(self) -> Team:
        return self.homeTeam

    def getAwayTeam(self) -> Team:
        return self.awayTeam

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

    def goal(self, scoringTeam: Team, scorer: Player, timeInSeconds: int):
        if self.homeTeam == scoringTeam:
            self.score.homeTeamScored()
        else:
            self.score.awayTeamScored()