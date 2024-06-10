MOD = 998244353

N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[0 for _ in range(K + 2)] for __ in range(N)]
for i in range(N):
    dp[i][1] = 1
for j in range(1, K + 2):
    if j - 1 <= A[0]:
        dp[0][j] = 1
    dp[0][j] = (dp[0][j] + dp[0][j - 1]) % MOD
for i in range(1, N):
    for j in range(2, K + 2):
        dp[i][j] = (dp[i - 1][j] - dp[i - 1][max(j - A[i] - 1, 0)] + MOD) % MOD
        dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD
print((dp[N - 1][K + 1] - dp[N - 1][K] + MOD) % MOD)
