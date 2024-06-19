INF = float("inf")

N, M = map(int, input().split())
a = [0 for _ in range(M)]
b = [0 for _ in range(M)]
d = [0 for _ in range(M)]
for i in range(M):
    a[i], b[i], d[i] = map(int, input().split())

dist = [[INF for _ in range(N)] for __ in range(N)]
for i in range(N):
    dist[i][i] = 0
for i in range(M):
    dist[a[i]][b[i]] = d[i]
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    if dist[u][v] == INF:
        print("INF")
    else:
        print(dist[u][v])
