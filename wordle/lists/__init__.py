from pathlib import Path

LIST_DIR = Path(__file__).parent

with open(LIST_DIR / 'wordle-answers.txt') as f:
    WORDLE_ANSWERS = [w.strip() for w in f.readlines()]

with open(LIST_DIR / 'wordle-guesses.txt') as f:
    WORDLE_GUESSES = [w.strip() for w in f.readlines()]

ANSWERS = WORDLE_ANSWERS
GUESSES = WORDLE_GUESSES
