import sys
from collections import defaultdict

read = sys.stdin.readline


# def BIT_sum(i: int, tree: list) -> int:
#     ans = 0
#     while i > 0:
#         ans += tree[i]
#         i -= (i & -i)
#     return ans
#
#
# def BIT_update(i: int, num: int, n: int, tree: list):
#     while i <= n:
#         tree[i] += num
#         i += (i & -i)


def solution():
    N, K = map(int, read().split())
    Map = defaultdict(int)

    # BIT_tree = [0] * (N + 1)
    tree = [0] * (N+1)
    inputs = list(map(int, read().split()))
    for idx, val in enumerate(inputs, start=1):
        # BIT_update(idx + 1, val, N, BIT_tree)
        tree[idx] = tree[idx-1] + val

    answer = 0
    for i in range(1, N + 1):
        # if K == (BIT_sum(i, BIT_tree)):
        if K == tree[i]:
            answer += 1

        # answer += Map[BIT_sum(i, BIT_tree) - K]
        answer += Map[tree[i]-K]
        # Map[BIT_sum(i, BIT_tree)] += 1
        Map[tree[i]] += 1

    print(answer)


solution()
