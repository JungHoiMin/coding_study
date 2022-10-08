class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current = self.head
        for c in string:
            if c not in current.children:
                current.children[c] = Node(c)
            current = current.children[c]
        current.data = string

    def search(self, string):
        current = self.head
        for c in string:
            current = current.children[c]

        if current.children:
            return False
        else:
            return True


def solution():
    n = int(input())
    tels = []
    trie = Trie()

    for _ in range(n):
        tel = input()
        tels.append(tel)
        trie.insert(tel)

    for tel in tels:
        if not trie.search(tel):
            print("NO")
            return
    print("YES")
    return


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solution()
