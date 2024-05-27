def pow_mod(a, l, m):
    if l == 0:
        return 1
    if l % 2 == 0:
        return pow_mod(a * a % m, l // 2, m)
    return a * pow_mod(a, l - 1, m) % m


def RollingHashMatch(text, pattern):
    base = 31
    h = 998244353
    t_len = len(text)
    p_len = len(pattern)
    t_hash = 0
    p_hash = 0
    for i in range(p_len):
        t_hash = (t_hash * base + ord(text[i])) % h
        p_hash = (p_hash * base + ord(pattern[i])) % h
    if t_hash == p_hash:
        print(0)
    for i in range(1, t_len - p_len + 1):
        t_hash = (
            t_hash * base
            + ord(text[i + p_len - 1])
            - ord(text[i - 1]) * pow_mod(base, p_len, h)
            + h
        ) % h
        if t_hash == p_hash:
            print(i)


S = input()
T = input()
RollingHashMatch(S, T)
