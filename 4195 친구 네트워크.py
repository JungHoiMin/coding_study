def find(x: str, root: dict):
    if root[x] != x:
        root[x] = find(root[x], root)
    return root[x]


def union(x: str, y: str, root: dict, value: dict):
    x = find(x, root)
    y = find(y, root)

    if x != y:
        root[x] = y
        value[y] += value[x]


def solution():
    F = int(input())
    root = dict()
    value = dict()

    for _ in range(F):
        name1, name2 = input().split(" ")
        if name1 not in root:
            root[name1] = name1
            value[name1] = 1
        if name2 not in root:
            root[name2] = name2
            value[name2] = 1

        union(name1, name2, root, value)
        print(value[find(name1, root)])


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solution()
