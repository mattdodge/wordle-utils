from collections import Counter
from wordle.guess.base import GuessingAlgorithm

""" A guessing algorithm that chooses a word based on the letter frequency of
remaining words """
class Frequency(GuessingAlgorithm):

    @classmethod
    def guess(cls, remaining_words):
        freq = cls.get_frequencies(remaining_words)
        scores = cls.score_words(remaining_words, freq)
        return sorted(scores, reverse=True)[0][1]

    @classmethod
    def get_frequencies(cls, remaining_words):
        char_counts = Counter()
        for w in remaining_words:
            char_counts.update(w)
        return char_counts

    @classmethod
    def score_words(cls, remaining_words, frequencies):
        word_scores = []
        for word in remaining_words:
            score = 0
            for pos, ch in enumerate(word):
                if ch in word[:pos]:
                    # If we've already seen this letter don't count it towards the score
                    continue
                score += frequencies[ch]
            word_scores.append((score, word))
        return word_scores
