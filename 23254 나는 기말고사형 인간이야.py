from queue import PriorityQueue


def solution():
    n, m = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    q = PriorityQueue()
    answer = 0

    for i in range(m):
        q.put((-min(100-As[i], Bs[i]), As[i], Bs[i]))

    for i in range(24*n):
        if q.empty():
            break
        priority, current_score, study_score = q.get()
        result = min(100, current_score + study_score)

        if result == 100:
            answer += 100
            continue

        q.put((-min(100-result, study_score), result, study_score))

    while not q.empty():
        answer += q.get()[1]

    print(answer)


solution()
