from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from FootballMatch.Player import Player

class Save(AbstractGameAction):
    def __init__(self, player: Player, timeInSeconds: int):
        super().__init__(player, timeInSeconds)