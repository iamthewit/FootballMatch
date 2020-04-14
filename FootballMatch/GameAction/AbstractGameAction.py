from abc import ABC

from FootballMatch.Player import Player

# TODO: add player position on pitch (PositionOnPitch or PitchPosition ???) class to record 
# where on the pitch the player was when the action occurred


class AbstractGameAction(ABC):
    def __init__(self, player: Player, time_in_seconds: int):
        self.player = player
        self.time_in_seconds = time_in_seconds
        super().__init__()
