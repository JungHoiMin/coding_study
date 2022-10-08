import sys
import heapq
from math import sqrt
sys.setrecursionlimit(10**5)


class Node:
    def __init__(self, n: int, x: float, y: float):
        self.n = n
        self.x = x
        self.y = y


def getDistance(node1: Node, node2: Node) -> float:
    return round(sqrt(pow((node2.x - node1.x), 2) + pow((node2.y - node1.y), 2)), 2)


def find(parents: list, x: int) -> int:
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


def union(parents: list, n1: int, n2: int):
    x = find(parents, n1)
    y = find(parents, n2)

    if x > y:
        parents[x] = y
    else:
        parents[y] = x


def solution():
    answer = 0
    n = int(input())
    parents = [i for i in range(n)]
    q = []
    nodes = [Node(0, *map(float, input().split()))]
    for i in range(1, n):
        new_node = Node(i, *map(float, input().split()))
        for node in nodes:
            heapq.heappush(q, (getDistance(node, new_node), node.n, new_node.n))
        nodes.append(new_node)

    while q:
        distance, n1, n2 = heapq.heappop(q)
        if find(parents, n1) != find(parents, n2):
            answer += distance
            union(parents, n1, n2)

    return answer


if __name__ == "__main__":
    print(solution())
