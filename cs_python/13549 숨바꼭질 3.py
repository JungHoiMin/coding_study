from collections import deque
from math import inf


def solution():
    N, K = map(int, input().split())
    q = deque()
    cost = [inf for _ in range(100001)]
    cost[N] = 0

    q.append(N)
    while q:
        current = q.popleft()
        if current == K:
            print(cost[current])
            break
        if 0 < current < 100001 and cost[current - 1] > cost[current]:
            cost[current - 1] = cost[current] + 1
            q.append(current - 1)
        if 0 < current * 2 < 100001 and cost[current * 2] > cost[current]:
            cost[current * 2] = cost[current]
            q.appendleft(current * 2)
        if 0 < current + 1 < 100001 and cost[current + 1] > cost[current]:
            cost[current + 1] = cost[current] + 1
            q.append(current + 1)


solution()
