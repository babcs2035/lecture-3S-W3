import resource
import sys

resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))
sys.setrecursionlimit(1000000)
MOD = 998244353


def lower_bound(i):
    l = i
    r = N
    while r - l > 1:
        m = (l + r) // 2
        if fish[m][0] - fish[i][0] >= X:
            r = m
        else:
            l = m
    return r


def dp(i, j):
    if i == N:
        return 1
    if memo[i][j] != -1:
        return memo[i][j]
    res = dp(i + 1, j)
    if j + fish[i][1] <= Y:
        res += dp(lower_bound(i), max(j, fish[i][1]))
        res %= MOD
    elif j == 0:
        res += 1
        res %= MOD
    memo[i][j] = res
    return memo[i][j]


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

fish = []
for i in range(N):
    fish.append((A[i], B[i]))
fish.sort()

memo = [[-1 for _ in range(Y + 1)] for __ in range(N)]
print(dp(0, 0))
