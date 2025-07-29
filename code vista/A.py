# m, n = [int(i) for i in input().split()]

# board = []
# for i in range(m):
#     row = [int(x) for x in input().split()]
#     board.append(row)

# sx, sy = [int(i) for i in input().split()]
# ex, ey = [int(i) for i in input().split()]
# mx, my = [int(i) for i in input().split()]

# jumps = [
#     (mx, my),
#     (my, -mx),
#     (-my, mx),
#     (-mx, -my)
# ]

# queue = [[sx, sy, 0]]
# visited = []
# for i in range(m):
#     visited.append([0]*n)
# visited[sx][sy] = 1

# found = False

# while len(queue) > 0:
#     x, y, steps = queue.pop(0)
#     if x == ex and y == ey:
#         print(steps)
#         found = True
#         break

#     for jx, jy in jumps:
#         nx = x + jx
#         ny = y + jy

#         if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
#             visited[nx][ny] = 1
#             queue.append([nx, ny, steps + 1])

# if not found:
#     print(-1)
