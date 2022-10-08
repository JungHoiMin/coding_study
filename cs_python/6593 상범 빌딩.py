from collections import deque

def solution() -> int:
    roads = []
    L, R, C = map(int, input().split())
    if L == R == C == 0:
        return 0

    for z in range(L):
        floor = []
        for y in range(R):
            temp = list(input())
            for x in range(len(temp)):
                if temp[x] == 'S':
                    start = (z, y, x)
                elif temp[x] == 'E':
                    end = (z, y, x)
            floor.append(temp)
        input()
        roads.append(floor)

    return bfs(start, end, roads)


def bfs(start: tuple, end: tuple, roads: list):
    block = "#"
    space = "."
    x = [0, 0, 0, 0, 1, -1]
    y = [0, 0, 1, -1, 0, 0]
    z = [1, -1, 0, 0, 0, 0]
    queue = deque()

    queue.append(start + (0,))
    while queue:
        current = queue.popleft()

        for i in range(6):
            zz = current[0] + z[i]
            yy = current[1] + y[i]
            xx = current[2] + x[i]
            distance = current[3] + 1
            if 0 <= zz < len(roads) and 0 <= yy < len(roads[0]) and 0 <= xx < len(roads[0][0]):
                if roads[zz][yy][xx] != block:
                    roads[zz][yy][xx] = block
                    if (zz, yy, xx) == end:
                        return distance
                    queue.append((zz, yy, xx, distance))
    return -1


if __name__ == "__main__":
    while True:
        x = solution()
        if x == -1:
            print("Trapped!")
        elif x == 0:
            break
        else:
            print("Escaped in {0} minute(s).".format(x))
