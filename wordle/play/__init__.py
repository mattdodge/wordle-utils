from copy import deepcopy
import re
from wordle.core.result import ensure_result, is_winner
from wordle.core.gameplay import filter_word_list
from wordle.guess import Frequency, Exhaustive, Random

class Solver():

    answers = []
    guesses = []

    diff_answers_guesses = True

    def solve(self):
        guesses = 0
        remaining_words = deepcopy(self.answers)

        while True:
            if len(remaining_words) == 0:
                print("I give up")
                break
            print(f"{len(remaining_words)} valid words remain")

            GuessingAlgorithm = self.get_guessing_algorithm(remaining_words)
            guess = GuessingAlgorithm.guess(remaining_words)
            guesses += 1
            certainty = round(1.0 / len(remaining_words) * 100)
            print(f"Guess: {guess.upper()} ({certainty}% certain)")
            result = self.gather_response(len(remaining_words[0]))
            if is_winner(result):
                print(f"Oh yeah, {guesses} guesses")
                break
            remaining_words = filter_word_list(remaining_words, guess, result)
        return guesses

    def get_guessing_algorithm(self, remaining_words):
        if len(remaining_words) < 50 and self.diff_answers_guesses:
            Exhaustive.guess_from_valid_only = False
            return Exhaustive

        # After narrowing our list a bit we can do an exhaustive
        # search for a good guess
        elif len(remaining_words) < 500:
            return Exhaustive

        # In the early rounds use a fast frequency analysis to guess
        elif len(remaining_words) < 1e6:
            return Frequency

        else:
            return Random

    def gather_response(self, strlen=5):
        resp = input("What's the result? (_/?/!) ")
        match = re.match(r'^[!?_]{' + str(strlen) + '}$', resp)
        if not match:
            print("Invalid response string, try again")
            return self.gather_response(strlen)
        return ensure_result(resp)
