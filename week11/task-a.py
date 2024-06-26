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


N, M = map(int, input().split())
a = [0 for _ in range(M)]
b = [0 for _ in range(M)]
d = [0 for _ in range(M)]
for i in range(M):
    a[i], b[i], d[i] = map(int, input().split())

edges = []
for i in range(M):
    edges.append((d[i], a[i], b[i]))
edges.sort()

tree = UnionFind(N)
ans = 0
for e in edges:
    if not tree.is_same_group(e[1], e[2]):
        tree.unite(e[1], e[2])
        ans += e[0]

print(ans)
