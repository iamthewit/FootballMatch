# TODO

Create rules around when actions can occur:
- pass_receive can only happen after pass_attempt
- interception can only occur after shot/pass_attempt
- etc
    
- When a player has the ball they can perform the following game actions:
    - kick_off
    - pass_attempt
    - run
    - shot
    
- When a player does not have the ball they can perform the following game actions:
    - deflection
    - interception
    - tackle
    - save (goal keepers only)
    - pass_receive
    - run (maybe reserve this one for players with the ball for the time being)

In order for a game to flow actions can only happen in certain circumstances:

- `Kick Off` must immediately be followed by a `Pass Attempt` made by the same `Player`

- `Pass Attempt` must be immediately be followed by either:
    - `Pass Receive` by another `Player` of the same `Team` as the `Player` attempting the pass
    - `Interception` by another `Player` of the opposing `Team`
    - `Deflection` by another `Player` of either `Team` 

- `Run` must be immediately followed by either:
    - `Pass Attempt` by the same `Player`
    - `Shot` by the same `Player`
    - `Tackle` by an opposing `Player`

- `Shot` must be immediately followed by either:
    - `Save` made by the opposing `Teams` `GoalKepper`
    - `Interception` by a `Player` of the opposing `Team`
    - `Deflection` by a `Player` of either `Team` 
    - `Goal` (Note: Goals are not game actions, need to think about how they are recorded in a `Game`)

Create `GameActionRule` abstract class and extend the class for each Game Action (`KickOffRule`, `PassAttemptRule`, `TackleRule`, etc)
A `GameActionRule` will take the following parameters:
    - Previous Game Action
    - Game Action
A `GameActionRule` will raise an `Error` if the given Game Action is invalid based on the Previous Game Action

Create a GameEngine class in App module that can be passed a game object and keeps track of all game actions.
Knowledge of the game and game actions will allow the game engine to determine what can happen after each action.
`GameEngine` should instantiate `GameActionRule` based on the given `GameAction` to determine if it is valid or not.
    - Create a `GameActionRuleFactory` take a `GameAction` as a param and return a `GameActionRule`
`GameEngine` should return a list of possible next actions after a valid action has occurred.

Game class ideas:
- possession
- this could be worked out based on all of the above events?
- player position when an action occurs
- substitutions
- time added on

Manager class:
- Team is managed by a manager

Player Class:
- designate player as captain
- ensure only one captain per team per match
- if captain is substituted make a new on field player captain

Formation classes:
- team has a formation
- formation is made up of players

Think about how to deal with offside:
- need to know all player positions when actions happen
- maybe player positions should be recorded independently of game actions?
- or maybe there should be an action for players that are not directly involved 
in the current play. Every second we could record each players PlayerPosition action?

App Ideas:
- Create an API to pull data from previous games

General:
- Add .env file
- Add overall config
- Add container