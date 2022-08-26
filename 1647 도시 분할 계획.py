# 크루스칼 알고리즘 사용
# 부모 노드 배열을 사용
# 사이클을 포함하지 않은 최소 간선 선택

def findParent(parents: list, x: int):
    if parents[x] == x:
        return x
    else:
        return findParent(parents, parents[x])


def renewParent(parents: list, x: int, y: int):
    x = findParent(parents, x)
    y = findParent(parents, y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


def solution():
    N, M = map(int, input().split())
    edges = []
    parents = [i for i in range(N)]
    cost = 0
    last = 0
    for _ in range(M):
        x, y, edge = map(int, input().split())
        edges.append((edge, x - 1, y - 1))
    edges.sort()

    for edge, x, y in edges:
        if findParent(parents, x) != findParent(parents, y):
            cost += edge
            last = edge
            renewParent(parents, x, y)

    return cost-last


print(solution())
