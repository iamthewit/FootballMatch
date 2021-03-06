from FootballMatch.GameAction.Rule.DeflectionRule import DeflectionRule
from FootballMatch.GameAction.Rule.InterceptionRule import InterceptionRule
from FootballMatch.GameAction.Rule.PassAttemptRule import PassAttemptRule
from FootballMatch.Player import Player
from FootballMatch.Score import Score
from FootballMatch.Team import Team

from FootballMatch.GameAction.Deflection import Deflection
from FootballMatch.GameAction.Interception import Interception
from FootballMatch.GameAction.KickOff import KickOff
from FootballMatch.GameAction.PassAttempt import PassAttempt
from FootballMatch.GameAction.PassReceive import PassReceive
from FootballMatch.GameAction.Run import Run
from FootballMatch.GameAction.Save import Save
from FootballMatch.GameAction.Shot import Shot
from FootballMatch.GameAction.Tackle import Tackle

from App.EventDispatcher import EventDispatcher


class Game:
    def __init__(self, home_team: Team, away_team: Team, score: Score, event_dispatcher: EventDispatcher):
        self.__homeTeam = home_team
        self.__awayTeam = away_team
        self.__score = score
        self.__eventDispatcher = event_dispatcher
        self.__actionLog = []

    def get_score(self) -> Score:
        return self.__score

    def get_home_team(self) -> Team:
        return self.__homeTeam

    def get_away_team(self) -> Team:
        return self.__awayTeam

    def goal(self, scoring_team: Team, scorer: Player, time_in_seconds: int):
        if self.__homeTeam == scoring_team:
            self.__score.home_team_scored()
        else:
            self.__score.away_team_scored()

    def get_last_action(self):
        return self.__actionLog[-1]

    # Game Actions

    def shot(self, player: Player, time_in_seconds: int, on_target: bool = False) -> Shot:
        shot = Shot(player, time_in_seconds, on_target)

        self.__eventDispatcher.dispatch_now(shot)
        self.__actionLog.append(shot)

        return shot

    def save(self, player: Player, time_in_seconds: int) -> Save:
        # TODO: check that player position is GoalKeeper
        save = Save(player, time_in_seconds)

        self.__eventDispatcher.dispatch_now(save)
        self.__actionLog.append(save)

        return save

    def tackle(self, player: Player, time_in_seconds: int) -> Tackle:
        tackle = Tackle(player, time_in_seconds)

        self.__eventDispatcher.dispatch_now(tackle)
        self.__actionLog.append(tackle)

        return tackle

    def pass_attempt(self, player: Player, time_in_seconds: int) -> PassAttempt:
        pass_attempt = PassAttempt(player, time_in_seconds)
        pass_attempt_rule = PassAttemptRule(pass_attempt, self.get_last_action())
        pass_attempt_rule.check()

        self.__eventDispatcher.dispatch_now(pass_attempt)
        self.__actionLog.append(pass_attempt)

        return pass_attempt

    def pass_receive(self, player: Player, time_in_seconds: int) -> PassReceive:
        pass_receive = PassReceive(player, time_in_seconds)

        self.__eventDispatcher.dispatch_now(pass_receive)
        self.__actionLog.append(pass_receive)

        return pass_receive

    def interception(self, player: Player, time_in_seconds: int) -> Interception:
        interception = Interception(player, time_in_seconds)
        interception_rule = InterceptionRule(interception, self.get_last_action())
        interception_rule.check()

        self.__eventDispatcher.dispatch_now(interception)
        self.__actionLog.append(interception)

        return interception

    def deflection(self, player: Player, time_in_seconds: int) -> Deflection:
        deflection = Deflection(player, time_in_seconds)
        deflection_rule = DeflectionRule(deflection, self.get_last_action())
        deflection_rule.check()

        self.__eventDispatcher.dispatch_now(deflection)
        self.__actionLog.append(deflection)

        return deflection

    def run(self, player: Player, time_in_seconds: int) -> Run:
        run = Run(player, time_in_seconds)

        self.__eventDispatcher.dispatch_now(run)
        self.__actionLog.append(run)

        return run

    # TODO
    # def freeKick(self, player: Player, timeInSeconds: int) -> FreeKick:
    #     pass

    # TODO
    # def penalty(self, player: Player, timeInSeconds: int) -> Penalty:
    #     pass

    # TODO
    # def corner(self, player: Player, timeInSeconds: int) -> Corner:
    #     pass

    # TODO
    # def playerPosition(self, player: Player, timeInSeconds: int, positionX: int, positionY: int) -> PlayerPosition:
    #     pass

    def kick_off(self, player: Player, time_in_seconds: int) -> KickOff:
        kick_off = KickOff(player, time_in_seconds)

        self.__eventDispatcher.dispatch_now(kick_off)
        self.__actionLog.append(kick_off)

        return kick_off
