from sys import stdin
Inf = 1000000000

def min_coins_greedy(coins, value):
    count = 0
    i = 0
    while value > 0:
        if value/coins[i] >= 1:
            add = int(value/coins[i])
            value = value%coins[i]
            count = count + add
        i += 1
    return count
        
def min_coins_dynamic(coins, value):
    count = [0]
    for i in range(len(count), value + 1):
        count.append(count[i-1] + 1)
        for coin in coins:
            if coin <= i and count[i-coin] + 1 < count[i]:
                count[i] = count[i-coin] + 1
    return count[value]

def can_use_greedy(coins):
    for i in range(1,len(coins)):
        if coins[i]%coins[i-1] != 0:
            return False
    return True

coins = []
for c in stdin.readline().split():
    coins.append(int(c))
coins.sort()
coins.reverse()
method = stdin.readline().strip()
if method == "graadig" or (method == "velg" and can_use_greedy(coins)):
    for line in stdin:
        print(min_coins_greedy(coins, int(line)))
else:
    for line in stdin:
        print(min_coins_dynamic(coins, int(line)))
