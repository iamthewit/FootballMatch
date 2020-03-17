import unittest

from FootballMatch.Score import Score


class ScoreTest(unittest.TestCase):
    def setUp(self):
        self.score = Score()

    def test_initialScore(self):
        assert(0 == self.score.get_home_team_score())

    def test_homeTeamScoring(self):
        self.score.home_team_scored()
        
        assert(1 == self.score.get_home_team_score())

    def test_awayTeamScoring(self):
        self.score.away_team_scored()
        
        assert(1 == self.score.get_away_team_score())

    def test_formattedScore(self):
        self.score.home_team_scored()
        self.score.away_team_scored()

        assert("1 - 1" == self.score.formatted_score())
