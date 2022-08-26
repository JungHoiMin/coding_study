from queue import PriorityQueue


def solution():
    q = PriorityQueue()

    n, m = map(int, input().split())
    temp = list(map(int, input().split()))
    answer = 0

    for num in temp:
        q.put(num)
        answer += num

    for _ in range(m):
        num1 = q.get()
        num2 = q.get()
        s = num1 + num2
        q.put(s)
        q.put(s)
        answer += s

    print(answer)


solution()
