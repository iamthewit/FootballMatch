from PositionInterface import PositionInterface

class Midfielder(PositionInterface):
    def __init__(self):
        self.name = 'Midfielder'

    def name(self) -> str:
        return self.name