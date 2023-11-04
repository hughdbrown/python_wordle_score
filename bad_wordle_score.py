from collections import Counter, defaultdict
from doctest import testmod

HIT, CLOSE, MISS = 'X', 'x', '.'

def get_score(word: str, guess: str) -> str: 
    """
    >>> get_score('beset', 'tepee')
    'xX.X.'
    >>> get_score('crane', 'crete')
    'XX..X'
    >>> get_score('crane', 'nacre')
    'xxxxX'
    >>> get_score('crane', 'slate')
    '..X.X'
    >>> get_score('crane', 'toils')
    '.....'
    >>> get_score('erase', 'chase')
    '..XXX'
    >>> get_score('eerie', 'breed')
    '.xxx.'
    >>> get_score('eerie', 'chase')
    '....X'
    >>> get_score('eerie', 'deter')
    '.X.xx'
    >>> get_score('erect', 'tepee')
    'xx.x.'
    >>> get_score('tepee', 'beset')
    '.X.Xx'
    >>> get_score('tepee', 'erect')
    'x.x.x'
    """
    word = word.lower()
    guess = guess.lower()
    score: str = ""

    if len(word) == len(guess):
        for pos, letter in enumerate(guess):
            if letter in word:
                if letter == word[pos]:
                    score += HIT
                else:
                    score += CLOSE
            else:
                score += MISS
    return score


if __name__ == '__main__':
    testmod()
