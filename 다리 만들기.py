from math import inf
import sys
sys.setrecursionlimit(10 ** 8)


def betweenDistance(bridge1: tuple, bridge2: tuple) -> int:
    x1, y1 = bridge1
    x2, y2 = bridge2
    distance = abs(x2 - x1) + abs(y2 - y1) - 1
    if distance <= 0:
        return inf
    else:
        return distance


def findSection(N: int, stack: list, x: int, y: int, visited: list, temp: set):
    if x > 0:
        if not visited[x - 1][y]:
            visited[x - 1][y] = True
            if stack[x - 1][y] == 1:
                temp.add((x - 1, y))
                findSection(N, stack, x - 1, y, visited, temp)
    if x < N - 1:
        if not visited[x + 1][y]:
            visited[x + 1][y] = True
            if stack[x + 1][y] == 1:
                temp.add((x + 1, y))
                findSection(N, stack, x + 1, y, visited, temp)
    if y > 0:
        if not visited[x][y - 1]:
            visited[x][y - 1] = True
            if stack[x][y - 1] == 1:
                temp.add((x, y - 1))
                findSection(N, stack, x, y - 1, visited, temp)
    if y < N - 1:
        if not visited[x][y + 1]:
            visited[x][y + 1] = True
            if stack[x][y + 1] == 1:
                temp.add((x, y + 1))
                findSection(N, stack, x, y + 1, visited, temp)

    return temp


def divideSection(N: int, stack: list, bridge: dict):
    visited = [[False] * N for _ in range(N)]
    current = 0
    for x in range(N):
        for y in range(N):
            if visited[x][y]:
                continue
            visited[x][y] = True
            if stack[x][y] == 1:
                current += 1
                bridge[current] = set()
                bridge[current].add((x, y))
                findSection(N, stack, x, y, visited, bridge[current])


def solution():
    N = int(input())
    stack = []
    bridge = dict()

    for i in range(N):
        temp = [*map(int, input().split())]
        stack.append(temp)

    divideSection(N, stack, bridge)

    min_distance = inf
    for i in range(1, len(bridge) + 1):
        for j in range(i + 1, len(bridge) + 1):
            for a in bridge[i]:
                for b in bridge[j]:
                    distance = betweenDistance(a, b)

                    if min_distance > distance:
                        min_distance = distance

    print(min_distance)


if __name__ == "__main__":
    solution()
