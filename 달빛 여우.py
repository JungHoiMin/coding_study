# 테스트 케이스는 통과하지만 시간초과
from math import inf


def Floyd_Warshall(N: int, forest: list) -> list:
    for k in range(N):
        for i in range(N):
            for j in range(N):
                forest[i][j] = min(forest[i][j], forest[i][k] + forest[k][j])
    return forest[0]


def dfs(forest: list, goal: int):
    stack = [(0, [0])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m, distance in enumerate(forest[n]):
                if m in path or distance is inf:
                    continue
                stack.append((m, path + [m]))

    min_value = inf
    run = False
    for path in result:
        current = 0
        sum_value = 0
        for node in path:
            if run:
                distance = forest[current][node] / 2
            else:
                distance = forest[current][node] * 2
            sum_value += distance
            run = not run
            current = node

        if min_value > sum_value:
            min_value = sum_value
        print(path, sum_value)
    return min_value


def WolfRun(N: int, forest: list) -> list:
    road = [0]

    for i in range(1, N):
        road.append(dfs(forest, i))

    return road


N, M = map(int, input().split())
forest = [[inf for _ in range(N)] for _ in range(N)]
for i in range(N):
    forest[i][i] = 0.0

for i in range(M):
    a, b, d = map(int, input().split())
    forest[a - 1][b - 1] = float(d)
    forest[b - 1][a - 1] = float(d)

fox = Floyd_Warshall(N, forest[:])
wolf = WolfRun(N, forest[:])

cnt = 0
for i in range(N):
    if fox[i] < wolf[i]:
        cnt += 1
print(cnt)
