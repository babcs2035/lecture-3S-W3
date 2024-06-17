import collections

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
A = [input() for _ in range(H)]
sy -= 1
sx -= 1
gy -= 1
gx -= 1

queue = collections.deque()
queue.append((sy, sx, 0))
visited = [[False for __ in range(W)] for _ in range(H)]
visited[sy][sx] = True
dist = [[0 for __ in range(W)] for _ in range(H)]
while len(queue) > 0:
    vy, vx, d = queue.popleft()
    dist[vy][vx] = d
    if vy == gy and vx == gx:
        print(d)
        break
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        xx = vx + dx
        yy = vy + dy
        if 0 <= xx < W and 0 <= yy < H and not visited[yy][xx] and A[yy][xx] == ".":
            queue.append((yy, xx, d + 1))
            visited[yy][xx] = True
