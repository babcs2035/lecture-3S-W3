class Queue:
    def __init__(self, size: int):
        self.queue = [None] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, v: int):
        if self.tail == self.head and self.queue[self.head] != None:
            print("queue is full")
            return
        self.queue[self.tail] = v
        self.tail = (self.tail + 1) % len(self.queue)

    def dequeue(self):
        if self.head == self.tail and self.queue[self.head] == None:
            print("queue is empty")
            return
        temp = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % len(self.queue)
        return temp


Q, K = map(int, input().split(" "))
q = Queue(K)
for _ in range(Q):
    temp = input().split(" ")
    if len(temp) == 1:
        res = q.dequeue()
        if res != None:
            print(res)
    else:
        a, b = map(int, temp)
        q.enqueue(b)
