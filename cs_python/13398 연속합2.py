from math import inf
def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(arr[0])
        return

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = arr[0]

    max_value = -inf
    for i in range(1, n):
        dp[0][i] = max(arr[i], arr[i] + dp[0][i - 1])
        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
        max_value = max(max_value, dp[0][i], dp[1][i])
    print(max_value)


solution()
