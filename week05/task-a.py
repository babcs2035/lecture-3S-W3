def shaker_sort(seq):
    right = len(seq) - 1
    left = 0

    swapped = 0
    cnt = 0
    while left < right:
        for i in range(left, right):
            if seq[i + 1] < seq[i]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = i
        right = swapped
        for i in range(right, left, -1):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                swapped = i
        left = swapped
        cnt += 1
    return cnt


N = int(input())
A = input().split()
A = [int(a) for a in A]
print(shaker_sort(A))
print(*A)
