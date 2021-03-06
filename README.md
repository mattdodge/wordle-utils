# Wordle Utils

Helper functions, word lists, and analysis tools for Wordle and other Wordle variants.

## Installation

```bash
pip install wordle-utils
```

## Basic Usage

To run a bot that solves wordle for you, just run the following from your terminal after installing the package:

```bash
solve_wordle
```

The bot will output guesses, input what the "result" of those guesses is. `_` is a miss/blank, `!` is a correct/green, and `?` is a wrong spot/yellow letter.


## Advanced Usage

This library can be used for more than just solving wordle automatically.

### Analysis

To see how many words were possible after a series of guesses use the `what_do_i_know` function. This takes the actual answer as well as some guesses that were made and returns the possible words after those guesses. This can be useful after completing the Wordle puzzle to see how well you narrowed down the possible word list.

In this example, the actual answer word was ROBOT. The two guesses made were LATER and TROUT. You can see that after these two guesses the only possible words remaining were ROBOT and WORST.

```python
from wordle.analysis import what_do_i_know

what_do_i_know('robot', 'later', 'trout')
# ['robot', 'worst']
```

### Library Functions

This library has some helper functions you can use in your own scripts. These will work for most Wordle variants.

**Result**

This library includes a `Result` enum (`wordle.core.result.Result`) for possible results of a guess. A result can be a miss, wrong spot, or correct. In most functions you can replace the enum with the shorthand string version of a result

* `Result.correct` / `'!'` - the letter appears in this exact spot in the answer
* `Result.wrong_spot` / `'?'` - the letter appears somewhere else in the answer
* `Result.miss` / `'_'` - the letter does not appear in the word

There is some interesting behavior when guesses or answers contain duplicate letters. The [test cases](https://github.com/mattdodge/wordle-utils/blob/master/wordle/tests/test_result.py) should give you a better idea of these. The behavior is meant to mimic the behavior of the actual Wordle game.

**get_result**

Given a guess and a known answer, return the "result" of the guess. This will be an array of `Result` objects.

For example, if the answer was ROBOT and the guess was TROUT:
```python
from wordle.core.gameplay import get_result

get_result('trout', 'robot')
# [Result.miss, Result.wrong_spot, Result.wrong_spot, Result.miss, Result.correct]
```

**filter_word_list**

Given a starting list of words, return a new filtered down word list based on a guess and its result. You can use this function to whiddle down a word list as more guesses and results are learned.

For example, assume the remaining words were CLAIM, EMAIL, IMAGE, and SIGMA. The player guessed STAIN and got a result of `__!!_`.

```python
from wordle.core.gameplay import filter_word_list

words = ['claim', 'email', 'image', 'sigma']
new_words = filter_word_list(words, 'stain', '__!!_')
# ['claim', 'email']
```

## Variants

This library supports Wordle variants as well, since many of the gameplay strategies and functions are the same.

### Mathler/Nerdle

These are both math based variants of Wordle where rather than guessing words you are guessing equations or expressions

* [Mathler](https://mathler.com) - the target answer is given to you, find an expression that equals it. Comes in [easy](https://easy.mathler.com) and [hard](https://hard.mathler.com) variants as well.
* [Nerdle](https://nerdlegame.com) - you provide a full 8-digit equation, expression on one side, an equals sign, and then the result on the other side.

To have the solving bot play either of these games, call their solve methods

```python
# Play Mathler (normal mode) with a target number of 314
from wordle.play.mathler import play_mathler
play_mathler(314)
```

```python
# Play Nerdle
from wordle.play.mathler import play_nerdle
play_nerdle()
```
