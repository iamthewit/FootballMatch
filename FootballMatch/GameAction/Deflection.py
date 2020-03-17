from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from FootballMatch.Player import Player


class Deflection(AbstractGameAction):
    def __init__(self, player: Player, time_in_seconds: int):
        super().__init__(player, time_in_seconds)
