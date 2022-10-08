def solution():
    n = int(input())
    visited = [False] * (n + 1)
    visited[0] = True
    team = [False] * (n + 1)
    team[0] = True

    pointer = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        if pointer[i] == i:
            team[i] = True
            visited[i] = True

    for i in range(1, n + 1):
        if visited[i]:
            continue
        current = i
        path = []
        while True:
            if visited[current]:
                if current in path:
                    start = path.index(current)
                    for s in range(start, len(path)):
                        team[path[s]] = True
                break
            path.append(current)
            visited[current] = True
            next_node = pointer[current]
            if next_node == i:
                for p in path:
                    team[p] = True
                break
            current = next_node
    answer = 0
    for i in range(1, n + 1):
        if not team[i]:
            answer += 1
    return answer


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(solution())
