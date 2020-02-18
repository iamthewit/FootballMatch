from PositionInterface import PositionInterface

class Defender(PositionInterface):
    def __init__(self):
        self.name = 'Defender'

    def name(self) -> str:
        return self.name