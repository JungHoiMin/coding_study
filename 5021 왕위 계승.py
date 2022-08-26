from collections import defaultdict
import sys

read = sys.stdin.readline


def dfs(family, people, baby, king):
    if not family[baby]:
        return people[baby]
    parent1, parent2 = family[baby]
    value = (dfs(family, people, parent1, king) + dfs(family, people, parent2, king))/2
    people[baby] = value
    return value


def solution():
    N, M = map(int, read().split())

    family = defaultdict(tuple)
    people = defaultdict(float)
    king = input()
    people[king] = 1.0

    for _ in range(N):
        baby, parent1, parent2 = read().split()
        family[baby] = (parent1, parent2)

    max_value = 0
    answer = ""
    for _ in range(M):
        name = input()
        value = dfs(family, people, name, king)
        if value:
            if max_value < value:
                max_value = value
                answer = name

    print(answer)


solution()
