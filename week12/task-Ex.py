INF = float("inf")


def dfs(s, e, f):
    if s == e:
        return f
    visited[s] = True
    for v in range(1, N + 1):
        if not visited[v] and capacity[s][v] > 0:
            f_new = dfs(v, e, min(f, capacity[s][v]))
            if f_new:
                capacity[s][v] -= f_new
                capacity[v][s] += f_new
                return f_new
    return 0


N, M, H = map(int, input().split())
u = [0 for _ in range(M)]
v = [0 for _ in range(M)]
h = [0 for _ in range(M)]
for i in range(M):
    u[i], v[i], h[i] = map(int, input().split())


capacity = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for k in range(1, H + 1):
    ans = 0
    capacity = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(M):
        capacity[u[i]][v[i]] = max(h[i] - k + 1, 0)
    while True:
        visited = [False for _ in range(N + 1)]
        res = dfs(1, N, INF)
        if res == 0:
            break
        ans += res
    print(ans)
