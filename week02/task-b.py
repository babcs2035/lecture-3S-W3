is_prime = [True for _ in range(2123456)]
is_prime[1] = False
k = 2
while k * k < 2123456:
    if is_prime[k]:
        t = k * 2
        while t < 2123456:
            is_prime[t] = False
            t += k
    k += 1

cnt = [0 for _ in range(2123456)]
for i in range(1, 2123456):
    if i % 2 and is_prime[i] and is_prime[(i + 1) // 2]:
        cnt[i] = 1
for i in range(len(cnt) - 1):
    cnt[i + 1] += cnt[i]

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split(" "))
    print(cnt[r] - cnt[l - 1])
