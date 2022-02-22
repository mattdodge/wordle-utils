from copy import deepcopy
import re
from wordle.core.result import ensure_result, is_winner
from wordle.core.gameplay import filter_word_list
from wordle.guess import Frequency, Exhaustive
from wordle.lists import ANSWERS

def solve(wordlist=ANSWERS):
    guesses = 0
    wordlist = deepcopy(wordlist)

    while True:
        if len(wordlist) == 0:
            print("I give up")
            break
        print(f"{len(wordlist)} valid words remain")

        # Choose a good guessing algorithm
        # If we're down to the end, look for any possible
        # word to guess, even wrong ones
        if len(wordlist) < 50:
            Exhaustive.guess_from_valid_only = False
            guess = Exhaustive.guess(wordlist)

        # After narrowing our list a bit we can do an exhaustive
        # search for a good guess
        elif len(wordlist) < 500:
            guess = Exhaustive.guess(wordlist)

        # In the early rounds use a fast frequency analysis to guess
        else:
            guess = Frequency.guess(wordlist)

        guesses += 1
        certainty = round(1.0 / len(wordlist) * 100)
        print(f"Guess: {guess.upper()} ({certainty}% certain)")
        result = gather_response()
        if is_winner(result):
            print(f"Oh yeah, {guesses} guesses")
            break
        wordlist = filter_word_list(wordlist, guess, result)
    return guesses

def gather_response(strlen=5):
    resp = input("What's the result? (_/?/!) ")
    match = re.match(r'^[!?_]{' + str(strlen) + '}$', resp)
    if not match:
        print("Invalid response string, try again")
        return gather_response(strlen)
    return ensure_result(resp)
