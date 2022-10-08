def solution():
    N, M, K = map(int, input().split())
    dp = [[1] * (M+1) for _ in range(N+1)]

    # a:가 'a'의 개수
    # z:가 'z'의 개수 라고 하면
    # 가능한 모든 수는: (a+z)!/(a!*z!) -> 중복 순열의 경우의 수 -> 재귀로 구했을 때 너무 느림 -> DP 사용
    for a in range(1, N+1):
        for z in range(1, M+1):
            dp[a][z] = dp[a-1][z] + dp[a][z-1]  # 현재 만들 수 있는 개수는 바로 직전까지 나온 것들에 뒤에 'a'를 붙이거나 'z'를 붙이는 것

    if dp[N][M] < K:
        print(-1)
    else:
        result = ""
        while True:
            if N == 0 or M == 0:
                result += 'a'*N
                result += 'z'*M
                break
            if K <= dp[N-1][M]:     # dp가 k보다 크다면 dp가 더 작아질 필요가 있다는 말이기 떄문에 'a'를 삽입
                result += 'a'
                N -= 1
            else:
                result += 'z'       # dp가 k보다 작다면 dp가 더 커져야 한다는 말이기 때문에 'z'를 삽입
                K -= dp[N-1][M]     # 'a'로 시작하는 경우들을 빼줘야 한다.
                M -= 1
        print(result)


solution()

# a = 2, z = 2, k = 5인경우
# zaaz 1
# zaza 2
# zzaa 3

# a\z   0   1   2
# 0     1   1   1
# 1     1   2   3
# 2     1   3   6

