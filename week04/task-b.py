def search(N, A, v):
    l = -1
    r = N
    while r - l > 1:
        m = (l + r) // 2
        if A[m] <= v:
            l = m
        else:
            r = m
    return r


N = int(input())
A = input().split()
A = [int(x) for x in A]

Q = int(input())
for _ in range(Q):
    v = int(input())
    r = search(N, A, v)
    if r == N:
        print("not exist")
    else:
        print(A[r])
