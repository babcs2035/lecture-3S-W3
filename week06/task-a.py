def create_table(pattern):
    table = [0 for _ in range(len(pattern) - 1)]
    j = 0
    for i in range(1, len(pattern) - 1):
        while pattern[i] != pattern[j] and j > 0:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def kmp(text, pattern):
    skip = create_table(pattern)
    t_len = len(text)
    p_len = len(pattern)
    t_i = 0
    p_i = 0
    while t_i < t_len and p_i < p_len:
        if text[t_i] == pattern[p_i]:
            t_i += 1
            p_i += 1
        elif p_i == 0:
            t_i += 1
        else:
            p_i = skip[p_i - 1]
    if p_i == p_len:
        return t_i - p_i
    return -1


S = input()
T = input()
print(kmp(S, T))
