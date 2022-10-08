def solution():
    n, k = map(int, input().split())

    coins = []
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        temp = int(input())
        if temp > k:
            continue
        coins.append(temp)

    for i in coins:
        for j in range(i, k + 1):
            dp[j] += dp[j - i]

    print(dp[k])


solution()
