BASE = 10**5
MOD = 10**9 + 7


def pow_mod(a, l, m):
    if l == 0:
        return 1
    if l % 2 == 0:
        return pow_mod(a * a % m, l // 2, m)
    return a * pow_mod(a, l - 1, m) % m


N = int(input())
K = []
V = []
for i in range(N):
    K.append(int(input()))
    V.append(list(map(int, input().split())))

cnt = [0 for _ in range(N)]
for i in range(N):
    for j in range(K[i]):
        cnt[i] += pow_mod(BASE, V[i][j], MOD)
        cnt[i] %= MOD

Q = int(input())
for _ in range(Q):
    n = int(input())
    x = list(map(int, input().split()))
    m = int(input())
    y = list(map(int, input().split()))

    c_x = 0
    c_y = 0
    D = set()
    for xx in x:
        c_x += cnt[xx - 1]
        c_x %= MOD
    for yy in y:
        c_y += cnt[yy - 1]
        c_y %= MOD
    if c_x == c_y:
        print("Yes")
    else:
        print("No")
