import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())

forest = []
cache = [[False for _ in range(M)] for _ in range(N)]
a = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    forest.append(temp)


def check(x: int, y: int):
    global forest, cache, flag
    cache[x][y] = True
    for i in range(x - 1, x + 2):
        if i < 0 or i >= N:
            continue
        for j in range(y - 1, y + 2):
            if j < 0 or j >= M:
                continue

            if forest[x][y] < forest[i][j]:
                flag = False
            if not cache[i][j] and forest[x][y] == forest[i][j]:
                check(i, j)


cnt = 0

for i in range(N):
    for j in range(M):
        if forest[i][j] > 0 and not cache[i][j]:
            flag = True
            check(i, j)
            if flag:
                a[i][j] = 1
                cnt += 1

print(cnt)