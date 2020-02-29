from abc import ABC

from Player import Player

class AbstractGameAction(ABC):
    def __init__(self, player: Player, timeInSeconds: int):
        self.player = player
        self.timeInSeconds = timeInSeconds
        super().__init__()