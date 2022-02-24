from wordle.lists import WORDLE_ANSWERS, WORDLE_GUESSES
from wordle.play import Solver


class WordleSolver(Solver):
    answers = WORDLE_ANSWERS
    guesses = WORDLE_GUESSES

def play_wordle():
    solver = WordleSolver()
    solver.solve()
