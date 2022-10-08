from math import inf

def solutionA(pumps: list, fireTrucks: list):
    f = 0
    p = 0
    min_value = inf
    min_idx = -1
    total = 0
    visited = [False] * len(pumps)
    while True:
        if f >= len(fireTrucks):
            break
        if p >= len(pumps):
            p = 0
            continue
        if visited[p]:
            p += 1
            continue
        current = abs(pumps[p] - fireTrucks[f])
        if min_value > current:
            min_value = current
            min_idx = p
            p += 1
        else:
            visited[min_idx] = True
            total += min_value
            min_value = inf
            min_idx = -1
            f += 1

    if min_value != inf:
        total += min_value

    return total


def solutionB(pumps: list, fireTrucks: list):
    fireTrucks = fireTrucks[::-1]
    f = 0
    p = 0
    min_value = inf
    min_idx = -1
    total = 0
    visited = [False] * len(pumps)
    while True:
        if f >= len(fireTrucks):
            break
        if p >= len(pumps):
            p = 0
            continue
        if visited[p]:
            p += 1
            continue
        current = abs(pumps[p] - fireTrucks[f])
        if min_value > current:
            min_value = current
            min_idx = p
            p += 1
        else:
            visited[min_idx] = True
            total += min_value
            min_value = inf
            min_idx = -1
            f += 1

    if min_value != inf:
        total += min_value

    return total


P, F = map(int, input().split())

pumps = list(map(int, input().split()))
fireTrucks = list(map(int, input().split()))

print(min(solutionA(pumps, fireTrucks), solutionB(pumps, fireTrucks)))
