from collections import deque


def solution():
    N, K = map(int, input().split())
    cnt = 0
    answer = []
    table = deque(i for i in range(1, N+1))
    while table:
        current = table.popleft()
        if cnt != K - 1:
            table.append(current)
        else:
            answer.append(current)
        cnt = (cnt + 1) % K

    print('<', end='')
    for i in range(N-1):
        print(answer[i], end=', ')
    print(answer[N-1], end='>')


solution()