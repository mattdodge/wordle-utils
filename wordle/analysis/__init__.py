from wordle.core.gameplay import get_result, filter_word_list
from wordle.lists import ANSWERS, GUESSES
from wordle.play import Solver

def what_do_i_know(answer, *guesses, wordlist=ANSWERS):
    """ Given a known answer and some guesses, which words are left """
    words = wordlist
    for guess in guesses:
        res = get_result(guess, answer)
        words = filter_word_list(words, guess, res)
    return words

def guess_scores(*guesses, wordlist=ANSWERS, guesslist=GUESSES):
    """ Give a score/grade for each guess compared to the optimal guess """
    answer = guesses[-1]
    solver = Solver()
    out = []
    words = wordlist
    for guess in guesses:
        algo = solver.get_guessing_algorithm(words)
        print(f"Evaluating {guess.upper()} using {algo.__name__}")
        best = algo.guess(words, guesslist)
        score = algo.score_guess(guess, words, guesslist)
        score = min(1, max(0, score))
        out.append({
            'best': best,
            'guess': guess,
            'score': score,
        })

        result = get_result(guess, answer)
        words = filter_word_list(words, guess, result)
    print()
    for guess in out:
        print(f"Guess {guess['guess'].upper()} - {_get_grade(guess['score'])} {guess['score'] * 100:.1f}% (Best: {guess['best'].upper()})")
    return out

def _get_grade(score):
    GRADES = [
        (0.98, 'A+'),
        (0.92, 'A'),
        (0.90, 'A-'),
        (0.88, 'B+'),
        (0.82, 'B'),
        (0.80, 'B-'),
        (0.78, 'C+'),
        (0.72, 'C'),
        (0.70, 'C-'),
        (0.68, 'D+'),
        (0.62, 'D'),
        (0.60, 'D-'),
        (0.00, 'F'),
    ]
    for grade_score, grade in GRADES:
        if grade_score < score:
            return grade
    return 'F'
