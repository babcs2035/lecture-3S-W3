class SegTree:
    def get_2pow(self, n):
        ans = 1
        while ans < n:
            ans *= 2
        return ans

    def initialize(self):
        start_i = self.leaf_start
        while start_i > 1:
            for i in range(start_i, start_i * 2, 2):
                parent_i = i // 2
                self.array[parent_i] = self.array[i] + self.array[i + 1]
            start_i //= 2

    def __init__(self, seq):
        size = self.get_2pow(len(seq))
        self.array = [0 for _ in range(2 * size)]
        self.leaf_start = size

        for i in range(self.leaf_start, self.leaf_start + len(seq)):
            self.array[i] = seq[i - self.leaf_start]

        self.initialize()

    def update(self, i, v):
        node_i = i + self.leaf_start
        self.array[node_i] = v

        while node_i > 1:
            parent_i = node_i // 2
            self.array[parent_i] = (
                self.array[parent_i * 2] + self.array[parent_i * 2 + 1]
            )
            node_i = parent_i

    def get_sum(self, l, r, k=1, le=0, re=-1):
        if re == -1:
            re = self.leaf_start
        if re < l or r <= le:
            return 0
        if l <= le and re < r:
            return self.array[k]
        return self.get_sum(l, r, 2 * k, le, (le + re - 1) // 2) + self.get_sum(
            l, r, 2 * k + 1, (le + re - 1) // 2 + 1, re
        )


Q = int(input())
queries = []
for _ in range(Q):
    queries.append(input().split(" "))

A = []
for query in queries:
    if len(query) == 2:
        A.append(int(query[1]))

A.sort()
s_tree = SegTree(A)


x = []
a = [-1, -1, -1]
for query in queries:
    if len(query) == 2:
        n = query[1]
        if a[0] == -1:
            a[0] = n
        elif a[1] == -1:
            if a[0] <= n:
                a[1] = n
            else:
                a[0], a[1] = n, a[0]
        elif a[2] == -1:
            if n <= a[0]:
                a[0], a[1], a[2] = n, a[0], a[1]
            elif n <= a[1]:
                a[1], a[2] = n, a[1]
            else:
                a[2] = n
        else:
            n


N = len(A)
m = N // 2
ans = []
for i in range(len(queries)):
    query = queries[len(queries) - 1 - i]
    if len(query) == 1:
        m = tree.get_mid_val(N)
        m_index = s_tree.find_index(m, N)
        res = (
            (N // 2 - 1) * m
            - s_tree.get_sum(0, N // 2)
            + s_tree.get_sum(N // 2, N)
            - (N - N // 2)
        )
    else:
        t = query[1]
        s_tree.update(s_tree.find_index(t, N), 0)
