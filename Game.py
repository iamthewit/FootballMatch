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
    
    def goal(self, scoringTeam: Team, scorer: Player, goalTimeInSeconds: int):
        if self.homeTeam == scoringTeam:
            self.score.homeTeamScored()
        else:
            self.score.awayTeamScored()

    def score(self):
        return Score