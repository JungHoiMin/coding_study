import sys

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if arr[i][j] != 1 and arr[i][k] == 1 and arr[k][j] == 1:
                    arr[i][j] = 1

    # 자기보다 큰놈 + 자기보다 작은 놈 == N-1
    # 자신을 포함한 행의 1의 개수가 자기보다 큰놈
    # 자신을 포함한 열의 1의 개수가 자기보다 작은놈
    answer = 0
    for i in range(1, N + 1):
        cnt = 0
        for j in range(1, N + 1):
            cnt += arr[i][j] + arr[j][i]

        if cnt == N - 1:
            answer += 1
    print(answer)


solution()
