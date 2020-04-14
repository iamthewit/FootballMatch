from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction
from FootballMatch.Player import Player


class Shot(AbstractGameAction):
    def __init__(self, player: Player, time_in_seconds: int, on_target: bool = False):
        super().__init__(player, time_in_seconds)
