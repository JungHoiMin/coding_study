from math import inf

def findMin(stack, resolve):
    min_value = inf
    min_index = -1
    for i, distance in enumerate(resolve):
        if stack[i]:
            continue
        if min_value>distance:
            min_index = i
            min_value = distance

    return min_index, min_value

def solution(N, road, K):
    answer = 0

    adj = [[inf for _ in range(N)] for _ in range(N)]
    for i, j, weight in road:
        if adj[i - 1][j -1] > weight:
            adj[i - 1][j - 1] = weight
            adj[j - 1][i - 1] = weight
    for i in range(N):
        adj[i][i] = 0

    stack = [False for _ in range(N)]
    stack[0] = True
    resolve = adj[0][:]

    while True:
        min_index, min_value = findMin(stack, resolve)
        if min_index == -1:
            break

        stack[min_index] = True
        for i in range(len(resolve)):
            temp = adj[min_index][i]
            if temp == inf:
                continue
            if resolve[i] > temp + min_value:
                resolve[i] = temp + min_value

    for i in resolve:
        if i <= K:
            answer += 1
    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
