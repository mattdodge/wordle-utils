from .base import GuessingAlgorithm
from random import choice

""" A guessing algorithm that simply chooses one of the remaining words at random """
class Random(GuessingAlgorithm):

    @classmethod
    def guess(cls, remaining_words):
        return choice(remaining_words)
