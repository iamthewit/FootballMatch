from PositionInterface import PositionInterface

class GoalKeeper(PositionInterface):
    def __init__(self):
        self.name = 'Goal Keeper'

    def name(self) -> str:
        return self.name