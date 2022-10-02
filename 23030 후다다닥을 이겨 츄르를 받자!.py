import sys
from math import inf
from heapq import heappush, heappop
input = sys.stdin.readline


def solution():
    N = int(input())
    noline = list(map(int, input().split()))
    stations = [[[] for _ in range(noline[i])] for i in range(N)]

    for i in range(N):
        for j in range(noline[i]):
            if j > 0:
                stations[i][j].append((i, j - 1))
            if j + 1 < noline[i]:
                stations[i][j].append((i, j + 1))

    M = int(input())
    for _ in range(M):
        P1, P2, Q1, Q2 = map(int, input().split())
        P1, P2, Q1, Q2 = P1-1, P2-1, Q1-1, Q2-1
        stations[P1][P2].append((Q1, Q2))
        stations[Q1][Q2].append((P1, P2))

    K = int(input())
    for _ in range(K):
        T, U1, U2, V1, V2 = map(int, input().split())
        U1, U2, V1, V2 = U1-1, U2-1, V1-1, V2-1
        times = [[inf] * (noline[i]) for i in range(N)]
        times[U1][U2] = 0
        q = []
        heappush(q, (U1, U2))
        while q:
            current_x, current_y = heappop(q)
            for next_x, next_y in stations[current_x][current_y]:
                if current_x == next_x and times[next_x][next_y] > times[current_x][current_y] + 1:
                    times[next_x][next_y] = times[current_x][current_y] + 1
                    heappush(q, (next_x, next_y))
                elif current_x != next_x and times[next_x][next_y] > times[current_x][current_y] + T:
                    times[next_x][next_y] = times[current_x][current_y] + T
                    heappush(q, (next_x, next_y))
        print(times[V1][V2])


solution()
