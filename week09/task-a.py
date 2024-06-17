import sys
import resource

sys.setrecursionlimit(1000000)
resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))


def dfs(i):
    if visited[i]:
        return
    visited[i] = True
    for v in G[i]:
        dfs(v)


N, M, S, T = map(int, input().split())
a = [0] * M
b = [0] * M
for i in range(M):
    a[i], b[i] = map(int, input().split())

G = [[] for _ in range(N + 1)]
for i in range(M):
    G[a[i]].append(b[i])
    G[b[i]].append(a[i])

visited = [False for i in range(N + 1)]
dfs(S)
if visited[T]:
    print("Yes")
else:
    print("No")
