from .base import GuessingAlgorithm
from random import choice

""" A guessing algorithm that simply chooses one of the remaining words at random """
class Random(GuessingAlgorithm):

    @classmethod
    def guess(cls, remaining_words, possible_guesses=None):
        return choice(possible_guesses or remaining_words)
