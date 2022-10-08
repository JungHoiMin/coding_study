import sys


def find(parents: list, x: int):
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
    answer = 0
    N, M = map(int, sys.stdin.readline().split())
    sex = list(sys.stdin.readline().split())
    rank = [0] * N
    parents = [i for i in range(N)]
    q = []
    cnt = 0

    for _ in range(M):
        u, v, d = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        if sex[u] != sex[v]:
            q.append((d, u, v))

    q.sort()

    for d, u, v in q:
        u = find(parents, u)
        v = find(parents, v)
        if u != v:
            union(parents, rank, u, v)
            answer += d
            cnt += 1

    if cnt + 1 != N:
        return -1
    return answer


if __name__ == "__main__":
    print(solution())
