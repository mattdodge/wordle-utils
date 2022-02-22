from copy import deepcopy
from wordle.core.gameplay import filter_word_list, get_result
from wordle.core.result import is_winner
from wordle.guess.base import GuessingAlgorithm
from wordle.lists import GUESSES

""" A guessing algorithm that performs an exhaustive search of all guesses

This algorithm will simulate the remaining word list after every possible guess. The
guess that leads to the smallest word list on average will be the guess
"""
class Exhaustive(GuessingAlgorithm):

    # By default, only simluate guesses from valid remaining words
    # In some cases it makes sense to guess a word that may not be correct in order
    # to narrow down letters. Set this variable to False to perform that behavior
    guess_from_valid_only = True

    @classmethod
    def guess(cls, remaining_words):
        if cls.guess_from_valid_only:
            guess_words = deepcopy(remaining_words)
        else:
            guess_words = deepcopy(GUESSES)

        strlen = len(remaining_words[0])

        # These represent the current guess and what its worst case and average case
        # is for number of remaining words after the guess
        guess = None
        best_worst_score = len(remaining_words) + 1
        best_total_score = len(remaining_words)**2

        for guess_word in guess_words:
            # If we have a lot of words left don't even consider guessing something
            # with a double letter in it
            if len(remaining_words) > 1000 and len(set(guess_word)) < strlen:
                continue

            # Figure out the worst case and average case for this particular guess word
            word_worst = 0
            word_total = 0
            for possible_answer in remaining_words:
                result = get_result(guess_word, possible_answer)
                # If our guess was exactly right there are no guesses left
                if is_winner(result):
                    continue
                new_words = len(filter_word_list(remaining_words, guess_word, result))
                word_total += new_words
                word_worst = max(new_words, word_worst)
                if word_total > best_total_score:
                    # It's already worse, no sense continuing
                    break

            # If the average word list is better, use this guess
            if word_total < best_total_score:
                guess = guess_word
                best_worst_score = word_worst
                best_total_score = word_total
            # in case of ties for avg word list, use the one with the lowest worst case
            elif word_total == best_total_score and word_worst < best_worst_score:
                guess = guess_word
                best_worst_score = word_worst
                best_total_score = word_total
        return guess
