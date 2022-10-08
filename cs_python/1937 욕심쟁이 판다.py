import sys
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    if check[x][y] != -1:
        return check[x][y]
    check[x][y] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < n and 0 <= new_y < n:
            if trees[new_x][new_y] > trees[x][y]:
                check[x][y] = max(check[x][y], dfs(new_x, new_y) + 1)

    return check[x][y]


n = int(input())
trees = [list(map(int, input().split())) for _ in range(n)]
check = [[-1]*n for _ in range(n)]

answer = 1
for x in range(n):
    for y in range(n):
        answer = max(answer, dfs(x, y))

print(answer)
