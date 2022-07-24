from collections import Counter
from wordle.guess.base import GuessingAlgorithm

""" A guessing algorithm that chooses a word based on the letter frequency of
remaining words """
class Frequency(GuessingAlgorithm):

    @classmethod
    def guess(cls, remaining_words, possible_guesses=None):
        possible_guesses = possible_guesses or remaining_words
        freq = cls.get_frequencies(remaining_words)
        scores = cls.score_words(possible_guesses, freq)
        return sorted(scores, reverse=True)[0][1]

    @classmethod
    def get_frequencies(cls, remaining_words):
        char_counts = Counter()
        for w in remaining_words:
            char_counts.update(w)
        return char_counts

    @classmethod
    def score_words(cls, remaining_words, frequencies):
        return [(cls.score_word(word, frequencies), word) for word in remaining_words]

    @classmethod
    def score_word(cls, word, frequencies):
        score = 0
        for pos, ch in enumerate(word):
            if ch in word[:pos]:
                # If we've already seen this letter don't count it towards the score
                continue
            score += frequencies[ch]
        return score

    @classmethod
    def score_guess(cls, guess, remaining_words, possible_guesses=None):
        possible_guesses = possible_guesses or remaining_words
        # Compare the score of the guess to the score of the best/worst possible guesses
        freq = cls.get_frequencies(remaining_words)
        scores = cls.score_words(possible_guesses, freq)
        scores = sorted(scores, reverse=True)
        best = scores[0][0]
        worst = scores[-1][0]
        actual = cls.score_word(guess, freq)
        if best == worst:
            return 1 if actual == best else 0
        return (actual - worst) / (best - worst)
