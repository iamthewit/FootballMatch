from FootballMatch.Club import Club
from FootballMatch.Position import PositionInterface

class Player:

    def __init__(
        self,
        number: int,
        name: str,
        position: PositionInterface,
        club: Club
    ):
        self.__number = number
        # make this a value object with first name, last name and shirt name
        self.__name = name
        self.__position = position

    def number(self) -> int:
        return self.number

    def name(self) -> str:
        return self.name

    def position(self) -> PositionInterface:
        return self.position
