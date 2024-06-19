import heapq

INF = float("inf")

N, M, S = map(int, input().split())
a = [0 for _ in range(M)]
b = [0 for _ in range(M)]
d = [0 for _ in range(M)]
for i in range(M):
    a[i], b[i], d[i] = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):
    G[a[i]].append((b[i], d[i]))

dist = [INF for _ in range(N)]
dist[S] = 0
visited = [False for _ in range(N)]
queue = []
heapq.heappush(queue, (0, S))
while queue:
    d, v = heapq.heappop(queue)
    if visited[v]:
        continue
    for e in G[v]:
        if dist[e[0]] > d + e[1]:
            dist[e[0]] = d + e[1]
            heapq.heappush(queue, (dist[e[0]], e[0]))
    visited[v] = True

for i in range(N):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
