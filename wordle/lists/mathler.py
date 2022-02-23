from math import isclose
from pathlib import Path
import re


def generate_words(sofar, remaining):
    """ Recursively generate a list of math expressions """
    if remaining == 0:
        # A word is only valid if it ends in a digit
        if sofar[-1].isdigit():
            return [sofar]
        else:
            return []

    words = []
    if not sofar:
        for i in range(1, 10):
            words += generate_words(str(i), remaining - 1)
        return words

    if sofar[-1].isdigit():
        words += generate_words(sofar + '+', remaining - 1)
        words += generate_words(sofar + '-', remaining - 1)
        words += generate_words(sofar + '*', remaining - 1)
        words += generate_words(sofar + '/', remaining - 1)

        # Also include a 0 here, we won't do leading zeroes this way
        words += generate_words(sofar + '0', remaining - 1)

    # Only start at 1, we don't want leading zeroes in numbers
    for i in range(1, 10):
        words += generate_words(sofar + str(i), remaining - 1)
    return words

def build_word_list(expressions, desired_length=None):
    wordlist = []
    for expr in expressions:
        if not any(['+' in expr, '-' in expr, '*' in expr, '/' in expr]):
            continue
        result = eval(expr)
        # Make sure it's an integer
        # Don't just do an isinstance check here, we might have weird Python floating
        if result < 0 or not isclose(round(result), result):
            continue
        result = str(round(result))
        if desired_length is None:
            wordlist.append(expr + '=' + result)
        elif len(expr) + 1 + len(result) == desired_length:
            wordlist.append(expr + '=' + result)
    return wordlist

def generate_all_expressions(target_length=5):
    exprs = generate_words("", target_length)
    wordlist = build_word_list(exprs)
    with open(Path(__file__).parent / f'expressions-{target_length}.txt', 'w+') as f:
        for word in wordlist:
            f.write(word + '\n')

def generate_all_equations(target_length=8):
    exprs = []
    for expr_len in range(3, target_length - 1):
        print(f"Generating {expr_len} letter expressions")
        exprs += generate_words("", expr_len)
    wordlist = build_word_list(exprs, target_length)
    with open(Path(__file__).parent / f'equations-{target_length}.txt', 'w+') as f:
        for word in wordlist:
            f.write(word + '\n')

with open(Path(__file__).parent / 'equations-6.txt') as f:
    EQUATIONS6 = [w.strip() for w in f.readlines()]

with open(Path(__file__).parent / 'equations-7.txt') as f:
    EQUATIONS7 = [w.strip() for w in f.readlines()]

with open(Path(__file__).parent / 'equations-8.txt') as f:
    EQUATIONS8 = [w.strip() for w in f.readlines()]

with open(Path(__file__).parent / 'expressions-5.txt') as f:
    EXPRESSIONS5 = [w.strip() for w in f.readlines()]

with open(Path(__file__).parent / 'expressions-6.txt') as f:
    EXPRESSIONS6 = [w.strip() for w in f.readlines()]

EXPRESSIONS7 = []
EXPRESSIONS8 = []

def load_big_files():
    """ Don't do this by default to save time/memory """
    global EXPRESSIONS7, EXPRESSIONS8
    try:
        with open(Path(__file__).parent / 'expressions-7.txt') as f:
            EXPRESSIONS7 = [w.strip() for w in f.readlines()]
    except FileNotFoundError:
        # Generate these on your own with generate_all_expressions(7)
        pass

    try:
        with open(Path(__file__).parent / 'expressions-8.txt') as f:
            EXPRESSIONS8 = [w.strip() for w in f.readlines()]
    except FileNotFoundError:
        # Generate these on your own with generate_all_expressions(8)
        pass


def get_target_words(expr_words, target_result):
    """ Get a list of expressions only for a given length and result """
    words = []
    rex = re.compile(f'^(.*)={target_result}$')
    for word in expr_words:
        m = rex.match(word)
        if m:
            words.append(m.group(1))
    return words
