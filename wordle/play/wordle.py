from wordle.lists import WORDLE_ANSWERS, WORDLE_GUESSES
from wordle.play import Solver
from wordle.analysis import guess_scores, get_grade


class WordleSolver(Solver):
    answers = WORDLE_ANSWERS
    guesses = WORDLE_GUESSES

def play_wordle():
    solver = WordleSolver()
    solver.solve()

def analyze_wordle():
    guesses = []
    while True:
        resp = input("Next guess? ")
        if not resp:
            break
        guesses.append(resp)

    scores = guess_scores(*guesses)
    print()
    for guess in scores:
        print(f"Guess {guess['guess'].upper()} - {get_grade(guess['score'])} {guess['score'] * 100:.1f}% (Best: {guess['best'].upper()})")
