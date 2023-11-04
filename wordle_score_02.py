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
    c_sum, g_sum = Counter(correct), defaultdict(list)
    for i, (c, g) in enumerate(zip(correct, guess)):
        if c == g:
            result[i] = 'X'
            c_sum[c] -= 1
        else:
            g_sum[g].append(i)
    for g, g_pos in g_sum.items():
        for _ in range(min(len(g_pos), c_sum[g])):
            i, g_pos = g_pos[0], g_pos[1:]
            result[i] = 'x'
    return "".join(result)

if __name__ == '__main__':
    testmod()
