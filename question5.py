from collections import Counter
def question5(word):
    if len(word) == 1:
        return 0
    charCounter = Counter(word)
    vals = [1 for val in charCounter.values() if val % 2 != 0]
    sumVals = sum(vals)
    if sumVals > 0:
        return sumVals - 1
    else:
        return 0

assert question5("abcb") == 1
assert question5("abab") == 0
assert question5("buhcgcgihmbqgspscdgz") == 7