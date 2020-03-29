from datetime import datetime

from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction


class LogEventToFile:
    def __init__(self):
        super().__init__()

    def handle(self, event: AbstractGameAction):
        # TODO: Store the log file name in an overall config/.env file
        with open('event-log.txt', 'a') as eventLog:
            # [Time (HH:MM:SS)] Game Minute:Game Seconds - Player Name - Action
            now = datetime.now()
            line = "[%s] %d:%02d - %s - %s" % (
                now.strftime("%X"),
                event.time_in_seconds / 60,
                event.time_in_seconds % 60,
                event.player.name(),
                type(event).__name__,
            )

            eventLog.write(line + "\n")
