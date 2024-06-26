import heapq

N, M = map(int, input().split())
a = [0 for _ in range(M)]
b = [0 for _ in range(M)]
for i in range(M):
    a[i], b[i] = map(int, input().split())

indeg = [0 for _ in range(N)]
G = [[] for _ in range(N)]
for i in range(M):
    indeg[b[i]] += 1
    G[a[i]].append(b[i])
for i in range(N):
    G[i].sort()

que = []
for i in range(N):
    if indeg[i] == 0:
        que.append(i)
heapq.heapify(que)
ans = []
while que:
    v = heapq.heappop(que)
    ans.append(v)
    for u in G[v]:
        indeg[u] -= 1
        if indeg[u] == 0:
            heapq.heappush(que, u)

if len(ans) == N:
    print(*ans)
else:
    print(-1)
