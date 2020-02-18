class Score:
    def __init__(self, homeTeamScore: int = 0, awayTeamScore: int = 0):
        self.homeTeamScore = homeTeamScore
        self.awayTeamScore = awayTeamScore

    def homeTeamScored(self):
        self.homeTeamScore += 1
    
    def awayTeamScored(self):
        self.awayTeamScore += 1

    def formattedScore(self) -> str:
        return "{} - {}".format(self.homeTeamScore, self.awayTeamScore)