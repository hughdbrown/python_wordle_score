from collections import Counter, defaultdict
from doctest import testmod


def wordle_score_n(correct, guess):
    """
    >>> wordle_score_n('beset', 'tepee')
    'xX.X.'
    >>> wordle_score_n('crane', 'crete')
    'XX..X'
    >>> wordle_score_n('crane', 'nacre')
    'xxxxX'
    >>> wordle_score_n('crane', 'slate')
    '..X.X'
    >>> wordle_score_n('crane', 'toils')
    '.....'
    >>> wordle_score_n('erase', 'chase')
    '..XXX'
    >>> wordle_score_n('eerie', 'breed')
    '.xxx.'
    >>> wordle_score_n('eerie', 'chase')
    '....X'
    >>> wordle_score_n('eerie', 'deter')
    '.X.xx'
    >>> wordle_score_n('erect', 'tepee')
    'xx.x.'
    >>> wordle_score_n('tepee', 'beset')
    '.X.Xx'
    >>> wordle_score_n('tepee', 'erect')
    'x.x.x'
    """
    result = ['.'] * 5

    # Table of character to indexes in `correct`
    # Example:
    #     corr('eerie') = {'e': {0, 1, 4}, 'i': {3}, 'r': {2}}
    corr = defaultdict(set)
    for i, c in enumerate(correct):
        corr[c].add(i)

    # Find the matches between `correct` and `guess`, remove index from corr
    # `corr` is not mutated in loop, so no need to take copy of `corr.items()`
    for c, indexes in corr.items():
        # Need to take a copy of `indexes` by casting to list
        # Otherwise, it is not safe to mutate `indexes` in the loop
        for i in list(indexes):
            if c == guess[i]:
                result[i] = 'X'
                indexes.remove(i)

    for i, (rc, gc) in enumerate(zip(result, guess)):
        if rc == '.' and (s := corr.get(gc)):
            result[i] = 'x'
            s.pop()

    return "".join(result)

if __name__ == '__main__':
    testmod()
