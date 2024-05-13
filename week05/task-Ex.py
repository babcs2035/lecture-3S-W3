import queue

N = int(input())
A = list(map(int, input().split()))

A_sorted = A.copy()
A_sorted.sort()

pos = dict()
for i in range(N):
    if pos.get(A_sorted[i]) is None:
        pos[A_sorted[i]] = queue.Queue()
    pos[A_sorted[i]].put(i)

sec = []
for i in range(N):
    p = pos[A[i]].get()
    sec.append([min(i, p), max(i, p)])
sec.sort()

ans = 0
if len(sec) > 0:
    l = sec[0][0]
    r = sec[0][1]
    for s in sec:
        ll = s[0]
        rr = s[1]
        if r < ll:
            if r - l >= 1:
                ans += r - l + 1
            l = ll
            r = rr
        else:
            r = max(r, rr)
    if r - l >= 1:
        ans += r - l + 1

print(ans)
