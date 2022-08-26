import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x: int, y: int, space: list, visited: list):
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if 0 <= xx < len(space) and 0 <= yy < len(space[0]) and not visited[xx][yy]:
            if space[xx][yy] != 0:
                space[xx][yy] += 1
            else:
                visited[xx][yy] = 1
                dfs(xx, yy, space, visited)


def meltCheese(space: list):
    for x in range(len(space)):
        for y in range(len(space[0])):
            if space[x][y] >= 3:
                space[x][y] = 0
            elif space[x][y] > 0:
                space[x][y] = 1

    return space


def checkCheese(space: list) -> bool:
    for i in space:
        if 1 in i:
            return True
    return False


def solution():
    N, M = map(int, input().split())
    space = []
    time = 0
    for _ in range(N):
        space.append(list(map(int, input().split())))
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    while checkCheese(space):
        dfs(0, 0, space, deepcopy(visited))
        meltCheese(space)
        time += 1
    return time


print(solution())
