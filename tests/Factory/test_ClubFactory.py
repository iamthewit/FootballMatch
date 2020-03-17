import unittest

from Factory.ClubFactory import ClubFactory
from FootballMatch.Club import Club


class ClubFactoryTest(unittest.TestCase):
    def test_create(self):
        club_factory = ClubFactory()
        club = club_factory.create()

        assert(isinstance(club, Club))
