MOD = 998244353


def pow_mod(n, m):
    if m == 1:
        return n
    elif m % 2:
        return pow_mod(n, m - 1) * n % MOD
    else:
        return pow_mod(n, m / 2) ** 2 % MOD


N, K = map(int, input().split(" "))

fact = [1]
for i in range(1, 200001):
    fact.append(fact[-1] * i % MOD)

ans = fact[N] * pow_mod(fact[N - K], MOD - 2) % MOD * pow_mod(fact[K], MOD - 2) % MOD
print(ans)
