import sys
from math import inf


def trace(i: int, j: int, prev: list) -> list:
    if prev[i][j] == 0:
        return []
    else:
        k = prev[i][j]
        return trace(i, k, prev) + [k] + trace(k, j, prev)


def solution():
    n = int(input())
    m = int(input())
    adj = [[inf] * (n + 1) for _ in range(n + 1)]
    prev = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        adj[i][i] = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if adj[a][b] > c:
            adj[a][b] = c

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if adj[i][j] > adj[i][k] + adj[k][j]:
                    adj[i][j] = adj[i][k] + adj[k][j]
                    prev[i][j] = k

    # 첫 번째 출력 조건
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(adj[i][j] if adj[i][j] != inf else 0, end=" ")
        print()

    # 두 번째 출력 조건
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if adj[i][j] == 0 or adj[i][j] == inf:
                print(0)
                continue

            result = [i] + trace(i, j, prev) + [j]
            print(len(result), end=" ")
            print(*result)


solution()
