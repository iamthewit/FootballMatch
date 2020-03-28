from FootballMatch.Club import Club
from FootballMatch.Player import Player


class Team:
    def __init__(self, club: Club, players: [], home: bool = True):
        if len(players) == 0:
            raise ValueError("Player list can not be empty.")

        for player in players:
            if not isinstance(player, Player):
                raise ValueError("Players must be instances of the 'Player' class.")

        self.__club = club
        self.__home = home
        self.__away = not home
        self.__players = players

    def club(self):
        return self.__club

    def home(self):
        return self.__home

    def away(self):
        return self.__away

    def players(self):
        return self.__players

    def __eq__(self, other):
        return self.club().name == other.club().name
