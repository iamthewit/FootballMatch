from random import randrange
from random import choice

from FootballMatch.Club import Club
from FootballMatch.Player import Player

from FootballMatch.Position.Defender import Defender
from FootballMatch.Position.Forward import Forward
from FootballMatch.Position.GoalKeeper import GoalKeeper
from FootballMatch.Position.Midfielder import Midfielder


class PlayerFactory:
    def __init__(self):
        super().__init__()

    def create_defender_for_club(self, club: Club):
        number = self.get_random_number()
        name = self.get_random_name()
        
        return Player(number, name, Defender(), club)

    def create_forward_for_club(self, club: Club):
        number = self.get_random_number()
        name = self.get_random_name()
        
        return Player(number, name, Forward(), club)

    def create_goal_keeper_for_club(self, club: Club):
        number = self.get_random_number()
        name = self.get_random_name()
        
        return Player(number, name, GoalKeeper(), club)

    def create_midfielder_for_club(self, club: Club):
        number = self.get_random_number()
        name = self.get_random_name()
        
        return Player(number, name, Midfielder(), club)

    def get_random_name(self):
        word_file_path = "/usr/share/dict/words"
        word_file = open(word_file_path)
        name = choice(word_file.read().splitlines())
        word_file.close()

        return name

    def get_random_number(self):
        return randrange(1, 99)
