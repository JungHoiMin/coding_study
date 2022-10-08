import sys
import heapq

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    queue = []
    for i in range(N):
        x = int(sys.stdin.readline())
        if x == 0:
            if not queue:
                print(0)
            else:
                value, isPlus = heapq.heappop(queue)
                if not isPlus:
                    value *= -1
                print(value)
        elif x > 0:
            heapq.heappush(queue, (x, True))
        else:
            heapq.heappush(queue, (-x, False))
