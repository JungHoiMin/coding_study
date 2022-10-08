import sys
from heapq import *
from math import inf

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def check(road, x, y):
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if road[xx][yy] == '#':
            return True
    return False


def dijkstra(start: tuple, end: tuple, H: int, W: int, road: list, distance: list) -> int:
    q = []
    distance[start[0]][start[1]] = 0
    heappush(q, (0, start[0], start[1]))

    while q:
        cost, x, y = heappop(q)
        checkXY = check(road, x, y)

        if distance[x][y] < cost:
            continue

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 < xx < H - 1 and 0 < yy < W - 1 and road[xx][yy] != '#':
                if checkXY and check(road, xx, yy):
                    new_cost = cost
                else:
                    new_cost = cost + 1
                if distance[xx][yy] > new_cost:
                    distance[xx][yy] = new_cost
                    heappush(q, (new_cost, xx, yy))
    return distance[end[0]][end[1]]


def solution():
    H, W = map(int, sys.stdin.readline().split())
    road = []
    for x in range(H):
        temp = list(sys.stdin.readline())
        road.append(temp)
        if 'S' in temp or 'E' in temp:
            for y in range(W):
                if temp[y] == 'S':
                    start = (x, y)
                elif temp[y] == 'E':
                    end = (x, y)
    distance = [[inf] * W for _ in range(H)]

    return dijkstra(start, end, H, W, road, distance)


if __name__ == "__main__":
    print(solution())
