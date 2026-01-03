# Rock Paper Scissors (Python)

This is a command-line Rock Paper Scissors game written in Python where a player competes against the computer.

## How the Game Works

- At the start of the program, the player is asked whether they want to continue or quit.
- If the player chooses to continue, the game begins.
- In each round, the player selects one option:
  - `rock`
  - `paper`
  - `scissors`
- The computer randomly selects one of the same options.
- The winner of each round is decided using the standard rules:
  - Rock beats Scissors
  - Scissors beats Paper
  - Paper beats Rock
- If both the player and the computer choose the same option, the round results in a draw, and no points are awarded.

## Scoring System

- Both the player and the computer start with a score of `0`.
- The winner of a round earns `1` point.
- Scores are displayed after every round.
- The game continues until either the player or the computer reaches a score of `3`.

## Winning Rule

- The first player to reach a score of `3` wins the game.
- Once a winner is declared, the game ends.

## Input Validation and Error Handling

- The game ensures the player enters a valid choice when starting the game (`yes` or `no`).
- During gameplay, only `rock`, `paper`, or `scissors` are accepted as valid inputs.
- If an invalid input is entered, an error message is shown, and the player is prompted again without affecting the score.

## How to Play

1. Run the Python file:
   ```bash
   python rock_paper_scissor.py

2. Choose `Yes` to start the game or `No` to exit.
3. Enter your move when prompted:
4. View the result of each round along with the updated scores.
5. The game ends when either the player or the computer reaches a score of `3`.

