def qsort(seq, left, right):
    if left >= right:
        return
    pivot = seq[right]
    j = left
    for i in range(left, right):
        if seq[i] <= pivot:
            seq[i], seq[j] = seq[j], seq[i]
            j += 1
    seq[j], seq[right] = seq[right], seq[j]
    if len(seq) == right - left + 1:
        print(*seq)
    qsort(seq, left, j - 1)
    qsort(seq, j + 1, right)


N = int(input())
A = list(map(int, input().split()))

qsort(A, 0, N - 1)
print(*A)
