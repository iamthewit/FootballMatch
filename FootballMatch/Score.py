class Score:
    def __init__(self, home_team_score: int = 0, away_team_score: int = 0):
        self.__homeTeamScore = home_team_score
        self.__awayTeamScore = away_team_score

    def get_home_team_score(self) -> int:
        return self.__homeTeamScore

    def get_away_team_score(self) -> int:
        return self.__awayTeamScore

    def home_team_scored(self):
        self.__homeTeamScore += 1
    
    def away_team_scored(self):
        self.__awayTeamScore += 1

    def formatted_score(self) -> str:
        return "{} - {}".format(self.__homeTeamScore, self.__awayTeamScore)
