from sys import stdin

Inf = float("inf")


def min_coins_greedy(coins, value):
    # SKRIV DIN KODE HER
    coin_count = 0
    i = 0
    while value > 0:
        if coins[i] <= value:
            value -= coins[i]
            coin_count += 1
        else:
            i += 1
    return coin_count


def min_coins_dynamic(coins, value):
    opt = [0 for i in range(0, value+1)]

    for i in range(1, value+1):
        min_val = Inf
        for j in range(0, len(coins)):
            if coins[j] <= i:
                min_val = min(min_val, opt[i - coins[j]])
                opt[i] = 1 + min_val
    return opt[value]


def can_use_greedy(coins):
    # bare returner False her hvis du ikke klarer aa finne ut
    # hva som er kriteriet for at den graadige algoritmen skal fungere
    # SKRIV DIN KODE HER
    for i in range(len(coins) - 1):
        if coins[i] % coins[i+1] != 0:
            return False
    return True


coins = [] #liste over myntene tilgjengelig i synkende rekkefoelge
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
