from collections import Counter
from wordle.core.result import Result, ensure_result

def get_result(guess, answer):
    """ Given a guess and a known answer, return what the result would be """
    assert len(guess) == len(answer)
    # Letters we still need to account for in the answer
    to_account = Counter(answer)
    out = [None] * len(guess)

    # First build exat matches and totally wrongs
    for pos, ch_guess, ch_answer in zip(range(len(guess)), guess, answer):
        if ch_guess == ch_answer:
            out[pos] = Result.correct
            to_account[ch_answer] -= 1
        elif ch_guess not in answer:
            out[pos] = Result.miss

    for pos, ch_guess in enumerate(guess):
        if out[pos]:
            continue
        elif ch_guess in answer and to_account[ch_guess]:
            out[pos] = Result.wrong_spot
            to_account[ch_guess] -= 1
        else:
            out[pos] = Result.miss
    return out

def filter_word_list(wordlist, guess, result):
    """ Filter down a list of possible words based on a guess and result """
    out = []
    result = ensure_result(result)
    for w in wordlist:
        # If the word was the answer, it would yield the same result
        if get_result(guess, w) == result:
            out.append(w)
    return out
