import math


def checkPalindrome(n: str) -> bool:  # 회문인지 판별
    if n == n[::-1]:  # 회문이면 True
        return True
    return False  # 회문이 아니면 False


def checkPrimeNumber(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())

answer = N

while True:
    if answer == 1:
        break

    if checkPalindrome(str(answer)):
        if checkPrimeNumber(answer):
            break

    answer += 1

print(answer)
