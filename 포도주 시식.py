def solution():
    n = int(input())
    if n < 3:
        if n == 1:
            return int(input())
        elif n == 2:
            a = int(input())
            b = int(input())
            return a + b

    arr = list()
    dp = list()
    for i in range(3):
        arr.append(int(input()))

    dp.append(arr[0])
    dp.append(arr[0] + arr[1])
    dp.append(max(arr[0] + arr[2], arr[1] + arr[2], dp[1]))

    for i in range(3, n):
        arr.append(int(input()))
        dp.append(max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i], dp[i-1]))

    return max(dp)


print(solution())
