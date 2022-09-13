def towPow(x):
    if x == 0:
        return 1
    if x == 1:
        return 2
    mid = towPow(x//2)
    if x % 2 == 0:
        return mid * mid % 1000000007
    else:
        return mid * mid * 2 % 1000000007


def solution():
    answer = 0
    N = int(input())
    menu = sorted(list(map(int, input().split())))
    for i in range(N):
        answer += menu[i] * (towPow(i)-towPow(N-i-1))   # 조합에서 최대값 - 조합에서 최솟값을 각각 더해야함 -> (고른 메뉴가 최대일때의 경우의수 - 최소일떄의 경우의 수) * 고른 메뉴
    answer = answer % 1000000007
    print(answer)


solution()
