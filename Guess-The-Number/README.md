# Guess the Number (1-20)

A small command-line guessing game written in Python. You try to guess the secret number between 1 and 20, and the program gives hints until you get it right.

## How it works

- You enter a number between 1 and 20.
- The game responds with:
  - `close` when your guess is within 3 of the secret number
  - `too low` when your guess is 4-13 below the secret
  - `too high` for other higher guesses
  - `out of limit` if your guess is outside the 1-20 range
- The game keeps asking until you guess correctly, then reports how many attempts you took.

## Run

Make sure you have Python 3 installed, then run:

```powershell
python "guess num.py"
```

## File

- `guess num.py` - main game script

## Example

```text
enter your guess between (1-20) : 10
close
enter your guess between (1-20) : 15
Correct! You took 2 attempts.
```

