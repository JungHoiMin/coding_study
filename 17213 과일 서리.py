def C(n, k) -> int:
    k = min(k, n - k)
    ja = 1
    mo = 1
    for i in range(k):
        ja *= (n - i)
    for i in range(k):
        mo *= (k - i)
    return int(ja // mo)


def H(n, k) -> int:
    return C(n + k - 1, k)


def solution():
    N = int(input())
    M = int(input())

    print(H(N, M-N))


solution()
