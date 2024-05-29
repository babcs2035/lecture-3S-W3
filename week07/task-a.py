import sys
import resource

resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))  # スタック領域を拡大
sys.setrecursionlimit(1000000)  # 再帰回数の上限を拡大


def dp(i):
    global h, memo
    if i == 0:
        return 0
    if i == 1:
        return abs(h[1] - h[0])
    if memo[i] != -1:
        return memo[i]
    memo[i] = min(dp(i - 1) + abs(h[i] - h[i - 1]), dp(i - 2) + abs(h[i] - h[i - 2]))
    return memo[i]


N = int(input())
h = list(map(int, input().split()))

memo = [-1 for _ in range(N)]
print(dp(N - 1))
