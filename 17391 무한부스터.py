from collections import deque


def solution():
    N, M = map(int, input().split())
    roads = []
    for i in range(N):
        temp = list(map(int, input().split()))
        roads.append(temp)

    visited = [[0]*M for _ in range(N)]

    print(bfs(roads, visited))


def bfs(roads: list, visited: list):
    x = [0, 1]
    y = [1, 0]
    queue = deque()
    queue.append((0, 0))

    while queue:
        current = queue.popleft()

        for i in range(2):
            xx, yy = current
            for _ in range(roads[current[0]][current[1]]):
                xx += x[i]
                yy += y[i]

                if xx < len(roads) and yy < len(roads[0]) and visited[xx][yy] == 0:
                    queue.append((xx, yy))
                    visited[xx][yy] = visited[current[0]][current[1]] + 1

    return visited[-1][-1]


if __name__ == "__main__":
    solution()
