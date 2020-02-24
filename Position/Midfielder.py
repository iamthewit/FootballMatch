from Position.PositionInterface import PositionInterface

class Midfielder(PositionInterface):
    def __init__(self):
        self.__name = 'Midfielder'

    def name(self) -> str:
        return self.name