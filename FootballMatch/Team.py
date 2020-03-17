from FootballMatch.Club import Club


class Team:
    def __init__(self, club: Club, home: bool = True):
        self.club = club
        self.home = home
        self.away = not home

    def __eq__(self, other):
        return self.club.name == other.club.name
