import unittest
from pprint import pprint

from Score import Score

class ScoreTest(unittest.TestCase):
    def setUp(self):
        self.score = Score()

    def test_initialScore(self):
        assert(0 == self.score.getHomeTeamScore())

    def test_homeTeamScoring(self):
        self.score.homeTeamScored()
        
        assert(1 == self.score.getHomeTeamScore())

    def test_awayTeamScoring(self):
        self.score.awayTeamScored()
        
        assert(1 == self.score.getAwayTeamScore())

    def test_formattedScore(self):
        self.score.homeTeamScored()
        self.score.awayTeamScored()

        assert("1 - 1" == self.score.formattedScore())
