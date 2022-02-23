from copy import deepcopy
import re
from wordle.core.result import ensure_result, is_winner
from wordle.core.gameplay import filter_word_list
from wordle.guess import Frequency, Exhaustive
from wordle.lists import ANSWERS, GUESSES

def solve(wordlist=ANSWERS, guesses=GUESSES, diff_answers_guesses=True):
    guesses = 0
    remaining_words = deepcopy(wordlist)

    while True:
        if len(remaining_words) == 0:
            print("I give up")
            break
        print(f"{len(remaining_words)} valid words remain")

        # Choose a good guessing algorithm
        # If we're down to the end, look for any possible
        # word to guess, even wrong ones
        if len(remaining_words) < 50 and diff_answers_guesses:
            Exhaustive.possible_guesses = guesses
            Exhaustive.guess_from_valid_only = False
            guess = Exhaustive.guess(remaining_words)

        # After narrowing our list a bit we can do an exhaustive
        # search for a good guess
        elif len(remaining_words) < 500:
            guess = Exhaustive.guess(remaining_words)

        # In the early rounds use a fast frequency analysis to guess
        else:
            guess = Frequency.guess(remaining_words)

        guesses += 1
        certainty = round(1.0 / len(remaining_words) * 100)
        print(f"Guess: {guess.upper()} ({certainty}% certain)")
        result = gather_response(len(remaining_words[0]))
        if is_winner(result):
            print(f"Oh yeah, {guesses} guesses")
            break
        remaining_words = filter_word_list(remaining_words, guess, result)
    return guesses

def gather_response(strlen=5):
    resp = input("What's the result? (_/?/!) ")
    match = re.match(r'^[!?_]{' + str(strlen) + '}$', resp)
    if not match:
        print("Invalid response string, try again")
        return gather_response(strlen)
    return ensure_result(resp)
