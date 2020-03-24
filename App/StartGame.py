import random
from App.EventBus import EventBus
from App.EventDispatcher import EventDispatcher
from Factory.ClubFactory import ClubFactory
from Factory.PlayerFactory import PlayerFactory
from FootballMatch.Game import Game
from FootballMatch.Score import Score
from FootballMatch.Team import Team


class StartGame:
    def __init__(self):
        # Generate 2 clubs
        club_factory = ClubFactory()

        home_club = club_factory.create()
        away_club = club_factory.create()

        # TODO:
        # Generate 2 managers

        # Generate 2 Teams
        home_team = Team(home_club)
        away_team = Team(away_club, False)

        # Generate 22 players
        player_factory = PlayerFactory()

        # Generate 2 goal keepers
        home_keeper = player_factory.create_goal_keeper_for_club(home_club)
        away_keeper = player_factory.create_goal_keeper_for_club(away_club)

        # Generate 8 defenders
        # 4 defenders for the home club
        home_defenders = []
        for i in range(0, 4):
            home_defender = player_factory.create_defender_for_club(home_club)
            home_defenders.append(home_defender)

        # 4 defenders for the away club
        away_defenders = []
        for i in range(0, 4):
            away_defender = player_factory.create_defender_for_club(away_club)
            away_defenders.append(away_defender)

        # Generate 8 midfielders
        # 4 midfielders for the home club
        home_midfielders = []
        for i in range(0, 4):
            home_midfielder = player_factory.create_midfielder_for_club(home_club)
            home_midfielders.append(home_midfielder)

        # 4 midfielders for the away club
        away_midfielders = []
        for i in range(0, 4):
            away_midfielder = player_factory.create_midfielder_for_club(away_club)
            away_midfielders.append(away_midfielder)
                
        # Generate 4 forwards
        # 4 forwards for the home club
        home_forwards = []
        for i in range(0, 4):
            home_forward = player_factory.create_forward_for_club(home_club)
            home_forwards.append(home_forward)

        # 4 forwards for the away club
        away_forwards = []
        for i in range(0, 4):
            away_forward = player_factory.create_forward_for_club(away_club)
            away_forwards.append(away_forward)

        home_players = home_defenders + home_forwards + home_midfielders + [home_keeper]
        away_players = home_defenders + home_forwards + home_midfielders + [home_keeper]
        all_players = home_players + away_players

        # Create a Game object
        score = Score()
        event_bus = EventBus()
        event_dispatcher = EventDispatcher(event_bus)

        game = Game(home_team, away_team, score, event_dispatcher)

        game_methods = [
            'interception',
            'pass_attempt',
            'pass_receive',
            'run',
            'save',
            'shot',
            'tackle'
        ]

        # TODO: add goal method - it is a special case, it has different parameters

        # Randomly call game action methods on Game object
        # until we reach 90 minutes worth of seconds
        for i in range(0, 90):
            method = random.choice(game_methods)
            player = random.choice(all_players)
            getattr(game, method)(player, i * 60)

        # Check the event log to see what happened...

        # TODO: Generate stats based on the events...
