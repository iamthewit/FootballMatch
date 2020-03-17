from FootballMatch.Position.PositionInterface import PositionInterface


class Defender(PositionInterface):
    def __init__(self):
        self.__name = 'Defender'

    def name(self) -> str:
        return self.__name
