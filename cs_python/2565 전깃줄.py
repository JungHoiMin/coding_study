
def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        s, e = map(int, input().split())
        arr.append((s, e))
    arr.sort()

    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if arr[i][1] > arr[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    print(n-max(dp))


if __name__ == "__main__":
    solution()
