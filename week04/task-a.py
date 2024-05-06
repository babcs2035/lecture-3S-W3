Q = int(input())

M = 100000
table = [-1 for _ in range(M)]

for _ in range(Q):
    a, b = map(int, input().split())
    if a == 0:
        flag = False
        for i in range(M):
            ii = (b % M + i) % M
            if table[ii] == -1:
                table[ii] = b
                flag = True
                break
        if not flag:
            print("error")

    else:
        flag = False
        for i in range(M):
            ii = (b % M + i) % M
            if table[ii] == -1:
                print("not found")
                flag = True
                break
            elif table[ii] == b:
                print("found")
                flag = True
                break
            else:
                continue
        if not flag:
            print("not found")
