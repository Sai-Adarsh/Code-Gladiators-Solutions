T = int(input())

import math
def seive(m, n):
    # generate seive
    seive = [True for _ in range(n + 1)]
    seive[0] = False
    seive[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if seive[i] == False:
            continue
        for pointer in range(i * i, n + 1, i):
            seive[pointer] = False
    primes = []
    for i in range(m, n + 1):
        if seive[i] == True:
            primes.append(i)

    return primes[-1] - primes[0] if primes else -1

for _ in range(T):
    m, n = list(map(int, input().split()))
    print(seive(m, n))