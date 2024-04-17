N = int(input())
x = [a for a in map(int, input().split(" "))]

x_sum = [0]
xi_sum = [0]
for i in range(len(x)):
    x_sum.append(x_sum[-1] + x[i])
    xi_sum.append(xi_sum[-1] + x[i] * (i + 1))

Q = int(input())
for _ in range(Q):
    L, R, A, B = map(int, input().split(" "))
    ans = (xi_sum[R] - xi_sum[L - 1]) * A + (x_sum[R] - x_sum[L - 1]) * B
    print(ans)
