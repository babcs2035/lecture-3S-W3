N, W = map(int, input().split())
w = [0 for _ in range(N)]
v = [0 for _ in range(N)]
for i in range(N):
    w[i], v[i] = map(int, input().split())

max_sum_v = 200 * 100 + 1
dp = [[float("inf") for _ in range(max_sum_v)] for __ in range(N)]
dp[0][v[0]] = w[0]
for i in range(N):
    dp[i][0] = 0
for i in range(1, N):
    for j in range(1, max_sum_v):
        if j >= v[i]:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v[i]] + w[i])
        else:
            dp[i][j] = dp[i - 1][j]

ans = 0
max_v = 0
for j in range(max_sum_v):
    if dp[N - 1][j] <= W:
        ans = j
print(ans)
