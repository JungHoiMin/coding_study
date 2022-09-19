
def solution():
    durumari = list(input())
    devil = list(input())
    engel = list(input())

    len_duru = len(durumari)
    len_bridge = len(devil)

    dp = [[[0] * len_bridge for _ in range(2)] for _ in range(len_duru)]
    answer = 0

    for i, c in enumerate(durumari):
        if i == 0:
            for j in range(len_bridge):
                if c == devil[j]:
                    dp[i][0][j] = 1
                if c == engel[j]:
                    dp[i][1][j] = 1
            continue
        for j in range(len_bridge):
            if c == devil[j]:
                cnt = 0
                for k in range(0, j):
                    if durumari[i - 1] == engel[k]:
                        cnt += dp[i-1][1][k]
                dp[i][0][j] = cnt
            if c == engel[j]:
                cnt = 0
                for k in range(0, j):
                    if durumari[i - 1] == devil[k]:
                        cnt += dp[i-1][0][k]
                dp[i][1][j] = cnt

    for i in range(len_bridge):
        answer += dp[len_duru - 1][0][i] + dp[len_duru - 1][1][i]
    print(answer)


solution()

