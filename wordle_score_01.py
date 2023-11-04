from collections import Counter, defaultdict
from doctest import testmod


def wordscore(actual, test):
    """
    >>> wordscore('beset', 'tepee')
    'xX.X.'
    >>> wordscore('crane', 'crete')
    'XX..X'
    >>> wordscore('crane', 'nacre')
    'xxxxX'
    >>> wordscore('crane', 'slate')
    '..X.X'
    >>> wordscore('crane', 'toils')
    '.....'
    >>> wordscore('erase', 'chase')
    '..XXX'
    >>> wordscore('eerie', 'breed')
    '.xxx.'
    >>> wordscore('eerie', 'chase')
    '....X'
    >>> wordscore('eerie', 'deter')
    '.X.xx'
    >>> wordscore('erect', 'tepee')
    'xx.x.'
    >>> wordscore('tepee', 'beset')
    '.X.Xx'
    >>> wordscore('tepee', 'erect')
    'x.x.x'
    """
    correct = Counter(
        p
        for p, t in zip(actual, test)
        if p == t
    )
    incorrect = defaultdict(list)
    for i, (p, t) in enumerate(zip(actual, test)):
        if p != t:
            incorrect[t].append(i)
    d = [
        "X" if p == t else "."
        for p, t in zip(actual, test)
    ]
    removed_poss = Counter(actual) - correct
    for t, n in removed_poss.items():
        for i in incorrect[t][:n]:
            d[i] = 'x'
    return "".join(d)


if __name__ == '__main__':
    testmod()

