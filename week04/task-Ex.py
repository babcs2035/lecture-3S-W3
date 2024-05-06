def check(N, K, A, x):
    l = 0
    r = 0
    s = A[0]
    c = 0
    while r < N:
        if s < x:
            r += 1
            if r < N:
                s += A[r]
        else:
            c += N - r
            s -= A[l]
            l += 1
    return c >= K


N, K = map(int, input().split())
A = [int(a) for a in input().split()]

l = 0
r = 1123456789
while r - l > 1:
    m = (l + r) // 2
    if check(N, K, A, m):
        l = m
    else:
        r = m
print(l)
