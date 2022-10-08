def dfs(n: int, graph: dict, visited: list):
    visited[0] = True
    visited[1] = 'A'

    for current in range(1, n + 1):
        current_node = current
        while False in visited:
            nextIdx = -1

            for node in graph[current_node]:
                if not visited[node]:
                    nextIdx = node
                    break

            if nextIdx == -1:
                break
            else:
                if visited[current_node] == 'A':
                    visited[nextIdx] = 'B'
                else:
                    visited[nextIdx] = 'A'
                current_node = nextIdx

    for i in range(1, n+1):
        for node in graph[i]:
            if visited[i] == visited[node]:
                return -1
    return 0


def solution():
    n, m = map(int, input().split())

    graph = dict()
    for i in range(n):
        graph[i + 1] = []
    visited = [False] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    if dfs(n, graph, visited) == -1:
        print('impossible')
    else:
        print('possible')


if __name__ == '__main__':
    testcase = int(input())
    for _ in range(testcase):
        solution()
