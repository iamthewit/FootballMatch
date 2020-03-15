from FootballMatch.GameAction.AbstractGameAction import AbstractGameAction

class LogEventToFile:
    def __init__(self):
        super().__init__()

    def handle(self, event: AbstractGameAction):
        # TODO: Store the log file name in an overall config/.env file
        with open('event-log.txt', 'a') as eventLog:
            # TODO: log more details

            # write the name of the events type to the log file
            eventLog.write(type(event).__name__ + "\n")