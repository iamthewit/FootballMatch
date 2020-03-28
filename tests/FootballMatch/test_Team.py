import unittest

from FootballMatch.Club import Club
from FootballMatch.Team import Team


class TestTeam(unittest.TestCase):
    def test_it_raises_value_error_for_empty_list(self):
        club = Club('Football Club Name')
        player_list = []
        with self.assertRaises(ValueError):
            Team(club, player_list)

    def test_it_raises_value_error_for_non_empty_list_without_player_instances(self):
        club = Club('Football Club Name')
        player_list = [1, 2, 3, "one", "two", "three"]
        with self.assertRaises(ValueError):
            Team(club, player_list)
