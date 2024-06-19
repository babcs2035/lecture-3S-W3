import heapq

INF = float("inf")


def dijkstra(day):
    dist = [INF for _ in range(N)]
    dist[0] = 0
    queue = []
    heapq.heappush(queue, (0, 0))
    ends = []
    visited[0] = False
    while queue:
        d, v = heapq.heappop(queue)
        if visited[v]:
            continue
        flag = False
        for e in G[v]:
            if dist[e[0]] > d + e[1]:
                if d + e[1] > K:
                    flag = True
                    continue
                dist[e[0]] = d + e[1]
                heapq.heappush(queue, (dist[e[0]], e[0]))
        visited[v] = True
        if ans[v] == -1:
            ans[v] = day
        if flag:
            ends.append(v)
    return ends


N, M, K = map(int, input().split())
u = [0 for _ in range(M)]
v = [0 for _ in range(M)]
l = [0 for _ in range(M)]
for i in range(M):
    u[i], v[i], l[i] = map(int, input().split())
    u[i] -= 1
    v[i] -= 1

G = [[] for _ in range(N)]
for i in range(M):
    G[u[i]].append((v[i], l[i]))
    G[v[i]].append((u[i], l[i]))

visited = [False for _ in range(N)]
ans = [-1 for _ in range(N)]
day = 1
while True:
    starts = dijkstra(day)
    if not starts:
        break
    for v in starts:
        G[0].append((v, 0))
        visited[v] = False
    day += 1

for i in range(N - 1):
    print(ans[i + 1])
