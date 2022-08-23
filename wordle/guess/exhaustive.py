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

    @classmethod
    def guess(cls, remaining_words, possible_guesses=None):
        guess_words = cls._get_possible_guesses(remaining_words, possible_guesses)

        # These represent the current guess and what its worst case and average case
        # is for number of remaining words after the guess
        guess = None
        best_worst_score = len(remaining_words) + 1
        best_total_score = len(remaining_words)**2

        for guess_word in guess_words:
            # If we have a lot of words left don't even consider guessing something
            # with a double letter in it
            strlen = len(remaining_words[0])
            if len(remaining_words) > 1000 and len(set(guess)) < strlen:
                continue

            word_worst, word_total = cls.get_guess_score(guess_word, remaining_words, best_total_score)

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

    @classmethod
    def get_guess_score(cls, guess, remaining_words, existing_best_total=None):
        # Figure out the worst case and average case for this particular guess word
        word_worst = 0
        word_total = 0
        for possible_answer in remaining_words:
            result = get_result(guess, possible_answer)
            # If our guess was exactly right there are no guesses left
            if is_winner(result):
                continue
            new_words = len(filter_word_list(remaining_words, guess, result))
            word_total += new_words
            word_worst = max(new_words, word_worst)
            if existing_best_total and word_total > existing_best_total:
                # It's already worse, no sense continuing
                break
        return word_worst, word_total

    @classmethod
    def score_guess(cls, guess, remaining_words, possible_guesses=None):
        better = worse = 0
        guess_worst, guess_total = cls.get_guess_score(guess, remaining_words)

        guess_words = cls._get_possible_guesses(remaining_words, possible_guesses)
        for guess_word in guess_words:
            word_worst, word_total = cls.get_guess_score(guess_word, remaining_words)

            if word_total < guess_total:
                better += 1
            elif word_total == guess_total and word_worst < guess_worst:
                better += 1
            elif word_total > guess_total:
                worse += 1
            elif word_total == guess_total and word_worst > guess_worst:
                worse += 1
        return worse / (better + worse)

    @classmethod
    def _get_possible_guesses(cls, remaining_words, possible_guesses):
        if len(remaining_words) <= 50 and len(possible_guesses) != 0:
            return possible_guesses
        return remaining_words
