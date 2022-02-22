from enum import Enum

class Result(Enum):
    miss = 0
    wrong_spot = 1
    correct = 2

def ensure_result(result):
    """ Helper function to accept strings or Result enums """
    if isinstance(result, Result):
        return result
    if isinstance(result, str):
        if len(result) > 1:
            return [ensure_result(i) for i in result]
        if result == '_':
            return Result.miss
        elif result == '?':
            return Result.wrong_spot
        elif result == '!':
            return Result.correct
        else:
            raise ValueError("Only _/?/! are supported for results")
    if isinstance(result, list):
        return [ensure_result(i) for i in result]
    raise TypeError("Results must be an enum or a string")

def is_winner(result):
    """ Is a result all correct """
    return all([r == Result.correct for r in result])
