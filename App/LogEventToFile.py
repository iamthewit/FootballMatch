from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction


class LogEventToFile:
    def __init__(self):
        super().__init__()

    def handle(self, event: AbstractGameAction):
        # TODO: Store the log file name in an overall config/.env file
        with open('event-log.txt', 'a') as eventLog:
            # Minute:Seconds - Player Name - Action
            line = "%d:%02d - %s - %s" % (
                event.timeInSeconds / 60,
                event.timeInSeconds % 60,
                event.player.name(),
                type(event).__name__
            )

            eventLog.write(line + "\n")
