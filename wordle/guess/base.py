class GuessingAlgorithm():

    @classmethod
    def guess(cls, remaining_words, possible_guesses=None):
        return NotImplemented

    @classmethod
    def score_guess(cls, guess, remaining_words, possible_guesses=None):
        """ Given some remaining words, tell us how good our guess was """
        return NotImplemented
