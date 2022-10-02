# min 함수 사용을 최소화하자 -> min 함수 사용 시 비교 연산만 하는 거 뿐만아니라 할당까지 하기 때문에 if 문을 사용할 때보다 시간이 약간 더 걸린다.
import sys


def solution():
    N, M = map(int, sys.stdin.readline().split())
    places = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if places[i][j] > places[i][k]+places[k][j]:
                    places[i][j] = places[i][k]+places[k][j]

    for i in range(M):
        A, B, C = map(int, input().split())
        if places[A-1][B-1] > C:
            print("Stay here")
        else:
            print("Enjoy other party")


solution()
