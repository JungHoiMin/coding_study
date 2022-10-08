def checkWord(w1: str, w2: str):
    diff = 0
    for c1, c2 in zip(w1, w2):
        if c1 != c2:
            diff += 1

    if diff == 1:
        return True
    else:
        return False


def solution(begin, target, words):
    answer = 0
    graph = {}
    words.append(begin)
    for key in words:
        for value in words:
            if checkWord(key, value):
                cache = graph.get(key)
                if cache is None:
                    graph[key] = set([value])
                else:
                    cache.add(value)

    temp = [target]
    start = 0
    while True:
        answer += 1
        len_temp = len(temp)
        for i in range(start, len_temp):
            cache = graph.get(temp[start])
            if cache is None:
                return 0
            for c in cache:

                print("진행중...")
                if c == begin:
                    return answer
                if not c in temp:
                    temp.append(c)
        start = len_temp


    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
