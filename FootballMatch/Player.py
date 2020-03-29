from FootballMatch.Club import Club
from FootballMatch.Position.PositionInterface import PositionInterface


class Player:
    def __init__(
        self,
        number: int,
        name: str,
        position: PositionInterface,
        club: Club
    ):
        self.__number = number
        # TODO: make this a value object with first name, last name and shirt name
        self.__name = name
        self.__position = position
        self.__club = club

    def number(self) -> int:
        return self.__number

    def name(self) -> str:
        return self.__name

    def position(self) -> PositionInterface:
        return self.__position

    def club(self) -> Club:
        return self.__club

    def __eq__(self, other):
        if (
            isinstance(other, Player) and
            self.number() == other.number() and
            self.name() == other.name() and
            self.position() == other.position() and
            self.club().name == other.club().name
        ):
            return True

        return False

