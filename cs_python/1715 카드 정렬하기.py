from queue import PriorityQueue


def solution():
    q = PriorityQueue()

    n = int(input())
    for i in range(n):
        q.put(int(input()))
    answer = 0

    for _ in range(n-1):
        num1 = q.get()
        num2 = q.get()
        s = num1 + num2
        answer += s
        q.put(s)

    print(answer)


solution()
