import math
def question1(change):
    coins = [25, 10, 5, 1]
    coinCount = 0
    for coin in coins:
        coinCount += math.floor(change / coin)
        change = change % coin
    return coinCount

assert question1(50) == 2
assert question1(40) == 3