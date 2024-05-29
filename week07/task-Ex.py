import resource

resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))  # スタック領域を拡大

MOD = 998244353

H, W, P = map(int, input().split())
N = int(input())
h = [0 for _ in range(N)]
w = [0 for _ in range(N)]
p = [0 for _ in range(N)]
for i in range(N):
    h[i], w[i], p[i] = map(int, input().split())

dp = [[[0 for _ in range(H + W + 1)] for __ in range(W)] for ___ in range(H)]
earn = [[0 for _ in range(W)] for __ in range(H)]
for i in range(N):
    earn[h[i] - 1][w[i] - 1] = p[i]

dp[0][0][P] = 1
for i in range(H):
    for j in range(W):
        for k in range(H + W + 1):
            next_p = min(k - 1 + earn[i][j], H + W)
            if next_p >= 0:
                if i + 1 < H:
                    dp[i + 1][j][next_p] += dp[i][j][k]
                    dp[i + 1][j][next_p] %= MOD
                if j + 1 < W:
                    dp[i][j + 1][next_p] += dp[i][j][k]
                    dp[i][j + 1][next_p] %= MOD

ans = 0
for k in range(H + W + 1):
    ans += dp[H - 1][W - 1][k]
    ans %= MOD
print(ans)
