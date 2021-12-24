# def dfs(v):
#     visited[v] = 1
#     print(v, end=' ')
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
#
# graph = [
#     [],
#     [2,3,8],
#     [1,7],
#     [1,4,5],
#     [3,5],
#     [3,4],
#     [7],
#     [2,6,8],
#     [1,7]
# ]
# visited = [0] * 9
# dfs(1)



# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
#
# def puddle(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         puddle(x - 1, y)
#         puddle(x, y - 1)
#         puddle(x + 1, y)
#         puddle(x, y + 1)
#         return True
#     else:
#         return False
#
#
# cnt = 0
# for i in range(n):
#     for j in range(m):
#         if puddle(i, j) == True:
#             cnt += 1
#
# print(cnt)

a = int(input())
a.s123ort()
print(a[-1])