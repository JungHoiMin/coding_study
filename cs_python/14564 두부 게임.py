def tofu(N: int, M: int, A: int, n: int) -> int:
    if n == M//2+1:
        return 0
    A = A - (M//2+1 - n)
    if A < 1:
        A += N

    if A > N:
        A -= N
    return A


def solution():
    N, M, A = map(int, input().split())
    while True:
        n = int(input())
        A = tofu(N, M, A, n)
        print(A)
        if A == 0:
            break


if __name__ == "__main__":
    solution()
