INF = 1123456780


class MaxHeap:
    def __init__(self, size):
        self.size = size + 1
        self.array = [-INF] * self.size
        self.last = 0

    def check_after_add(self, i):
        if i < 2:
            return
        if self.array[i] > self.array[i // 2]:
            self.array[i], self.array[i // 2] = self.array[i // 2], self.array[i]
            self.check_after_add(i // 2)

    def check_after_remove(self, i):
        if i * 2 >= self.size:
            return
        if self.array[i * 2] >= self.array[i * 2 + 1]:
            if self.array[i] < self.array[i * 2]:
                self.array[i], self.array[i * 2] = self.array[i * 2], self.array[i]
                self.check_after_remove(i * 2)
        else:
            if self.array[i] < self.array[i * 2 + 1]:
                self.array[i], self.array[i * 2 + 1] = (
                    self.array[i * 2 + 1],
                    self.array[i],
                )
                self.check_after_remove(i * 2 + 1)

    def add(self, v: int):
        if self.last != self.size:
            self.last += 1
            self.array[self.last] = v
            self.check_after_add(self.last)

    def remove(self):
        if self.last != 0:
            temp = self.array[1]
            self.array[1] = self.array[self.last]
            self.array[self.last] = -INF
            self.last -= 1
            self.check_after_remove(1)
            return temp


Q = int(input())
h = MaxHeap(112345)
for _ in range(Q):
    temp = input().split(" ")
    if len(temp) == 1:
        res = h.remove()
        if res != None:
            print(res)
    else:
        a, b = map(int, temp)
        h.add(b)
