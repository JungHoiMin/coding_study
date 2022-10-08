def solution():
    T = int(input())
    if T % 10 != 0:
        return -1,
    T //= 10
    M = T // 6
    A = M // 5
    B = M - (A * 5)
    C = T - (M * 6)
    return A, B, C


if __name__ == "__main__":
    print(*solution())
