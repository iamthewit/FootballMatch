from random import randrange
from random import choice

from FootballMatch.Club import Club
from FootballMatch.Player import Player

from FootballMatch.Position.Defender import Defender
from FootballMatch.Position.Forward import Forward
from FootballMatch.Position.GoalKeeper import GoalKeeper
from FootballMatch.Position.Midfielder import Midfielder

from pprint import pprint

class PlayerFactory:
    def __init__(self):
        super().__init__()

    def getRandomName(self):
        wordFilePath = "/usr/share/dict/words"
        wordFile = open(wordFilePath)
        name = choice(wordFile.read().splitlines())
        wordFile.close()

        return name

    def createDefenderForClub(self, club: Club):
        number = randrange(1, 99)
        name = self.getRandomName()
        
        return Player(number, name, Defender(), club)