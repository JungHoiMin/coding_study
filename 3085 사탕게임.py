def explore(N: int, graph: list):
    cnt_Max = 0
    for i in range(N):
        cnt = 0
        prev = 'X'
        for j in range(N):
            if prev != graph[i][j]:
                cnt_Max = max(cnt_Max, cnt)
                cnt = 0
                prev = graph[i][j]
            cnt += 1
        cnt_Max = max(cnt_Max, cnt)

    for j in range(N):
        cnt = 0
        prev = 'X'
        for i in range(N):
            if prev != graph[i][j]:
                cnt_Max = max(cnt_Max, cnt)
                cnt = 0
                prev = graph[i][j]
            cnt += 1
        cnt_Max = max(cnt_Max, cnt)
    return cnt_Max


def solution():
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    cnt_Max = 0

    for i in range(N):
        for j in range(N):
            if i != N - 1:
                graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
                cnt_Max = max(explore(N, graph), cnt_Max)
                graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            if j != N - 1:
                graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
                cnt_Max = max(explore(N, graph), cnt_Max)
                graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]

    cnt_Max = max(explore(N, graph), cnt_Max)
    print(cnt_Max)


solution()
