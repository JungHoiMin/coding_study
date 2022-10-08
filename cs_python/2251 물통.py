from collections import deque


def visit(a, b, visited):
    if not visited[a][b]:
        visited[a][b] = True
        return False
    else:
        return True


def xtoy(x, y, Y):
    total = x + y
    temp = Y - total
    if temp >= 0:
        return 0, total
    else:
        return -temp, Y


def bfs(A: int, B: int, C: int):
    answer = set()
    queue = deque()
    queue.append((0, 0, C))
    visited = [[False] * 201 for _ in range(201)]
    while queue:
        a, b, c = queue.popleft()
        if a == 0:
            answer.add(c)

        # A->B
        newA, newB = xtoy(a, b, B)
        if not visit(newA, newB, visited):
            queue.append((newA, newB, c))

        # A->C
        newA, newC = xtoy(a, c, C)
        if not visit(newA, b, visited):
            queue.append((newA, b, newC))

        # B->A
        newB, newA = xtoy(b, a, A)
        if not visit(newA, newB, visited):
            queue.append((newA, newB, c))

        # B->C
        newB, newC = xtoy(b, c, C)
        if not visit(a, newB, visited):
            queue.append((a, newB, newC))

        # C->A
        newC, newA = xtoy(c, a, A)
        if not visit(newA, b, visited):
            queue.append((newA, b, newC))

        # C->B
        newC, newB = xtoy(c, b, B)
        if not visit(a, newB, visited):
            queue.append((a, newB, newC))

    return list(answer)


def solution():
    A, B, C = map(int, input().split())

    answer = bfs(A, B, C)
    answer.sort()
    return answer


if __name__ == "__main__":
    print(*solution())
