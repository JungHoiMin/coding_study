import sys

sys.setrecursionlimit(10 ** 6)


def find(parents: list, x: int) -> int:
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents: list, rank: list, x: int, y: int):
    x = find(parents, x)
    y = find(parents, y)

    if rank[x] > rank[y]:
        parents[y] = x
    else:
        parents[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def solution():
    N, M = map(int, sys.stdin.readline().split())
    s, e = map(int, sys.stdin.readline().split())
    s, e = s - 1, e - 1
    parents = [i for i in range(N)]
    rank = [0] * N
    q = []
    for _ in range(M):
        h1, h2, k = map(int, sys.stdin.readline().split())
        q.append((k, h1 - 1, h2 - 1))

    q.sort(reverse=True)
    for k, h1, h2 in q:
        if find(parents, h1) == find(parents, h2):
            continue

        union(parents, rank, h1, h2)

        if find(parents, s) == find(parents, e):
            return k

    return 0


if __name__ == "__main__":
    print(solution())
