from wordle.lists.mathler import get_target_words
from wordle.play import Solver

class MathlerSolver(Solver):
    pass

def play_mathler_easy(target_answer):
    from wordle.lists.mathler import EXPRESSIONS5
    wordlist = get_target_words(EXPRESSIONS5, target_answer)
    solver = MathlerSolver()
    solver.answers = wordlist
    solver.solve()

def play_mathler(target_answer):
    from wordle.lists.mathler import EXPRESSIONS6
    wordlist = get_target_words(EXPRESSIONS6, target_answer)
    solver = MathlerSolver()
    solver.answers = wordlist
    solver.solve()

# TODO: Support parentheses operators
def play_mathler_hard(target_answer):
    from wordle.lists.mathler import load_big_files
    print("Loading wordlist...")
    load_big_files()
    from wordle.lists.mathler import EXPRESSIONS8
    wordlist = get_target_words(EXPRESSIONS8, target_answer)
    solver = MathlerSolver()
    solver.answers = wordlist
    solver.solve()

def play_nerdle():
    from wordle.lists.mathler import EQUATIONS8
    solver = MathlerSolver()
    solver.answers = EQUATIONS8
    solver.solve()
