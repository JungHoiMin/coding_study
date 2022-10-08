class Node:
    def __init__(self, key):
        self.key = key
        self.data = None
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for c in string:
            if c not in current_node.children:
                current_node.children[c] = Node(c)
            current_node = current_node.children[c]
        current_node.data = string

    def starts_with(self, prefix, length):
        current_node = self.head
        words = []

        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return 0

        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    if len(node.data) == length:
                        words.append(node.data)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        return len(words)


def solution(words, queries):
    answer = []
    trie = Trie()
    backTrie = Trie()
    for word in words:
        trie.insert(word)
        trie.insert(word[::-1])

    set_queries = set(queries)
    dict_queries = dict()

    for q in set_queries:
        len_q = len(q)
        removeQ = q.replace('?', '')
        if q[0] == '?':
            dict_queries[q] = backTrie.starts_with(removeQ[::-1], len_q)
        else:
            dict_queries[q] = trie.starts_with(removeQ, len_q)

    for q in queries:
        answer.append(dict_queries[q])
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
