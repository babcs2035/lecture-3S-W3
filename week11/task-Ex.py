import sys
import resource

resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))  # スタック領域を拡大
sys.setrecursionlimit(1000000)  # 再帰回数の上限を拡大


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0 for _ in range(n)]

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i != j:
            if self.height[i] < self.height[j]:
                i, j = j, i
            self.parent[j] = i
            if self.height[i] == self.height[j]:
                self.height[i] += 1

    def is_same_group(self, i, j):
        return self.find(i) == self.find(j)


def dfs(v, max_c):
    visited[v] = True
    max_edge[v] = max_c
    for u, c in G[v]:
        if not visited[u]:
            dfs(u, max(max_c, c))


N, M = map(int, input().split())
u = [0 for _ in range(M)]
v = [0 for _ in range(M)]
c = [0 for _ in range(M)]
for i in range(M):
    u[i], v[i], c[i] = map(int, input().split())

edges = []
for i in range(M):
    edges.append((c[i], u[i], v[i]))
    edges.append((c[i], v[i], u[i]))
edges.sort()

tree = UnionFind(N + 1)
G = [[] for _ in range(N + 1)]
G_sum = 0
for e in edges:
    if not tree.is_same_group(e[1], e[2]):
        tree.unite(e[1], e[2])
        G[e[1]].append((e[2], e[0]))
        G[e[2]].append((e[1], e[0]))
        G_sum += e[0]

visited = [False for _ in range(N + 1)]
max_edge = [float("inf") for _ in range(N + 1)]
dfs(1, 0)

Q = int(input())
for _ in range(Q):
    ve, co = map(int, input().split())
    print(G_sum + co - max_edge[ve])
