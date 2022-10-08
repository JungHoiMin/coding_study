from math import inf


def trace(i: int, j: int, prev: list) -> int:
    if prev[i][j] == 0:
        return j
    else:
        k = prev[i][j]
        return trace(i, k, prev)


def solution():
    n, m = map(int, input().split())
    arr = [[inf] * (n + 1) for _ in range(n + 1)]
    prev = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        n1, n2, cost = map(int, input().split())
        arr[n1][n2] = cost
        arr[n2][n1] = cost
    for i in range(1, n + 1):
        arr[i][i] = 0
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]
                    prev[i][j] = k
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][j] == 0 or arr[i][j] == inf:
                print('-', end=" ")
            else:
                result = trace(i, j, prev)
                print(result, end=' ')
        print()


solution()
