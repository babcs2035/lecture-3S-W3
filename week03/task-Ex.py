INF = 1123456789


class Heap:
    def __init__(self, size):
        self.size = size + 1
        self.array = [INF] * self.size
        self.last = 0
        self.sum = 0

    def check_after_add(self, i):
        if i < 2:
            return
        if self.array[i] < self.array[i // 2]:
            self.array[i], self.array[i // 2] = self.array[i // 2], self.array[i]
            self.check_after_add(i // 2)

    def check_after_remove(self, i):
        if i * 2 >= self.size:
            return
        if self.array[i * 2] <= self.array[i * 2 + 1]:
            if self.array[i] > self.array[i * 2]:
                self.array[i], self.array[i * 2] = self.array[i * 2], self.array[i]
                self.check_after_remove(i * 2)
        else:
            if self.array[i] > self.array[i * 2 + 1]:
                self.array[i], self.array[i * 2 + 1] = (
                    self.array[i * 2 + 1],
                    self.array[i],
                )
                self.check_after_remove(i * 2 + 1)

    def add(self, v: int):
        if self.last != self.size:
            self.last += 1
            self.sum += v
            self.array[self.last] = v
            self.check_after_add(self.last)

    def remove(self):
        if self.last != 0:
            temp = self.array[1]
            self.array[1] = self.array[self.last]
            self.sum -= temp
            self.array[self.last] = INF
            self.last -= 1
            self.check_after_remove(1)
            return temp

    def get_size(self):
        return self.last

    def get_sum(self):
        return self.sum

    def get_min(self):
        return self.array[1]


Q = int(input())
h_min = Heap(Q)
h_max = Heap(Q)
for _ in range(Q):
    temp = input().split(" ")
    if len(temp) == 1:
        m = h_max.get_min()
        ans = (m * h_min.get_size() + h_min.get_sum()) + (
            h_max.get_sum() - m * h_max.get_size()
        )
        print(ans)
    else:
        v = int(temp[1])
        if h_min.get_size() + h_max.get_size() == 0:
            h_max.add(v)
        elif h_min.get_size() == h_max.get_size():
            if -h_min.get_min() <= v:
                h_max.add(v)
            else:
                h_max.add(-h_min.remove())
                h_min.add(-v)
        else:
            if v <= h_max.get_min():
                h_min.add(-v)
            else:
                h_min.add(-h_max.remove())
                h_max.add(v)
