from datetime import datetime

from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from FootballMatch.Player import Player

class Shot(AbstractGameAction):
    def __init__(self, player: Player, timeInSeconds: int, onTarget: bool):
        super().__init__(player, timeInSeconds)