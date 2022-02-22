from wordle.core.gameplay import get_result, filter_word_list
from wordle.lists import ANSWERS

def what_do_i_know(answer, *guesses):
    """ Given a known answer and some guesses, which words are left """
    words = ANSWERS
    for guess in guesses:
        res = get_result(guess, answer)
        words = filter_word_list(words, guess, res)
    return words
