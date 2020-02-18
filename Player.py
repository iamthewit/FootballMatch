from Club import Club
from PositionInterface import PositionInterface

class Player:

    def __init__(
        self,
        number: int,
        name: str,
        position: PositionInterface,
        club: Club
    ):
        self.number = number
        # make this a value object with first name, last name and shirt name
        self.name = name
        self.position = position

    def number(self) -> int:
        return self.number

    def name(self) -> str:
        return self.name

    def position(self) -> PositionInterface:
        return self.position
