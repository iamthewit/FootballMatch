class Score:
    def __init__(self, homeTeamScore: int = 0, awayTeamScore: int = 0):
        self.__homeTeamScore = homeTeamScore
        self.__awayTeamScore = awayTeamScore

    def getHomeTeamScore(self) -> int:
        return self.__homeTeamScore

    def getAwayTeamScore(self) -> int:
        return self.__awayTeamScore

    def homeTeamScored(self):
        self.__homeTeamScore += 1
    
    def awayTeamScored(self):
        self.__awayTeamScore += 1

    def formattedScore(self) -> str:
        return "{} - {}".format(self.__homeTeamScore, self.__awayTeamScore)