N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False for _ in range(S + 1)] for __ in range(N)]
for i in range(N):
    if i == 0:
        dp[i][0] = True
        dp[i][A[i]] = True
    else:
        for j in range(S + 1):
            if dp[i - 1][j]:
                dp[i][j] = True
                if j + A[i] <= S:
                    dp[i][j + A[i]] = True

if dp[N - 1][S]:
    print("Yes")
else:
    print("No")
