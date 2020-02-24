from Position.PositionInterface import PositionInterface

class Forward(PositionInterface):
    def __init__(self):
        self.__name = 'Forward'

    def name(self) -> str:
        return self.name