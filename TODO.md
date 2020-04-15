# TODO

WIP:
    - Add GameActionRules for:
        - KickOff
        - PassReceive
        - Rune
        - Save
        - Shot
        - Tackle

Ideas:

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

Game Actions:
    - Whistle (Kick Off, Half Time, Full Time, Foul)
        - Separate classes for each type or one class with a param for the type 
    - CollectLooseBall
        - Think of a better name
        - Can occur after a Deflection

Game class ideas:
- possession
    - this could be worked out based on all of the above events?
- player position when an action occurs
- substitutions
- time added on
- update stats after ever game action

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

Decide if a deflection can be intercepted?
- How else would another player pick up the ball after a deflection?
- Maybe a new action to 'collect' a loose ball?

Commentary:
- Create a commentary event listener
    - Listen for all actions, generate commentary based on actions

Referee Class

App Ideas:
- Create an API to pull data from previous games

General:
- Add .env file
- Add overall config
- Add container