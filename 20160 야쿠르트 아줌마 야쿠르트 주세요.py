# 경로중 같은 곳이 발견되면 그 뒤는 무조건 야쿠르트를 받을 수 있다 -> 이후 경로중 제일 작은 노드를 반환
import sys
from math import inf
import heapq


def dijkstra(graph: list, start: int, stop: int) -> list | float:
    queue = []
    distances = [inf] * (len(graph) + 1)
    distances[start] = 0
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue

        for new_node, new_distance in graph[current_node]:
            if distances[new_node] > current_distance + new_distance:
                distances[new_node] = current_distance + new_distance
                heapq.heappush(queue, (distances[new_node], new_node))

    if stop == -1:
        return distances

    return distances[stop]


def solution():
    answer = inf
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append([v, w])
        graph[v].append([u, w])

    ms = list(map(int, sys.stdin.readline().split()))
    me = int(sys.stdin.readline())

    me_distance = dijkstra(graph, me, -1)

    total = 0
    current = ms[0]
    for i in range(10):
        distance = dijkstra(graph, current, ms[i])
        if distance == inf:
            continue
        total += distance
        current = ms[i]
        if total >= me_distance[ms[i]]:
            answer = min(answer, ms[i])

    if answer == inf:
        return -1
    else:
        return answer


if __name__ == "__main__":
    print(solution())
