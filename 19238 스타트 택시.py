from collections import deque
from copy import deepcopy
import heapq


class Taxi:
    def __init__(self, x, y):
        self.x = x - 1
        self.y = y - 1


class Customer:
    def __init__(self, number, N, x, y, goalX, goalY, road):
        self.number = number
        self.x = x - 1
        self.y = y - 1
        self.goalX = goalX - 1
        self.goalY = goalY - 1
        self.distance = findDistance(N, self.x, self.y, self.goalX, self.goalY, road)


# bfs를 통해 출발지에서 목적지 까지 최적 거리 계산
def findDistance(N: int, x: int, y: int, goalX: int, goalY: int, road: list):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    q = deque([(x, y, 0)])  # 큐에 출발지 좌표와 거리 삽입
    road[x][y] = 1  # 출발지
    while q:
        cur = q.popleft()
        if cur[0] == goalX and cur[1] == goalY: # 목적지에 도착했는지 확인
            return cur[2]
        for i in range(4):  # 현재위치 기준 하 좌 상 우 형태로 탐색
            xx = dx[i] + cur[0]
            yy = dy[i] + cur[1]
            if 0 <= xx < N and 0 <= yy < N and road[xx][yy] != 1:   # 이동할 수 있으면 이동
                road[xx][yy] = 1
                q.append((xx, yy, cur[2] + 1))


# 목적지들 중 가장 가까운 거리를 찾는 함수로 택시가 손님 찾을 때 사용
def findCustomer(N: int, taxi: Taxi, customers: list, visited: list, road: list):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    currentVisited = visited[:] # 실제 손님을 태우기 전 임의로 손님들을 태우러 다녀봄
    for i, customer in enumerate(customers):
        if visited[i]:
            continue
        road[customer.x][customer.y] = str(i)   # 손님 자리에 손님번호 문자열로 입력
    heap = []
    q = deque([(taxi.x, taxi.y, 0)])
    if road[taxi.x][taxi.y] != 0:   # 만약 손님이 제자리에 있다면 가장 가까운 손님 안 찾고 바로 태움
        number = int(road[taxi.x][taxi.y])
        distance = 0
        taxi.x = customers[number].goalX
        taxi.y = customers[number].goalY
        visited[number] = True
        return number, distance

    road[taxi.x][taxi.y] = 1    # 택시 현재 위치

    while q:    # 가장 가까운 손님 찾기 시작
        cur = q.popleft()
        if not False in currentVisited: # 만약 모든 손님을 확인했으면 반복문 종료
            break
        for i in range(4):  # 현재위치 기준 하 좌 상 우 형태로 탐색
            xx = dx[i] + cur[0]
            yy = dy[i] + cur[1]
            if 0 <= xx < N and 0 <= yy < N and road[xx][yy] != 1:   # 방문할 수 있다면 실행
                if road[xx][yy] != 0:   # 만약 손님이라면 힙에 넣음
                    heapq.heappush(heap, (cur[2] + 1, road[xx][yy]))
                    currentVisited[int(road[xx][yy])] = True
                road[xx][yy] = 1    # 위치 방문
                q.append((xx, yy, cur[2] + 1))

    if not heap:
        return -1, -1
    number = int(heap[0][1])    # 최소 힙에서 가장 가까운 손님 번호 꺼냄
    distance = heap[0][0]   # 최소 힙에서 가장 가까운 손님의 거리 꺼냄
    for i in range(1, len(heap)):   # 만약 거리가 같은 손님이 있다면 행이 더 작은 손님 선택
        if distance < heap[i][0]:
            break
        equalDistanceNumber = int(heap[i][1])
        if customers[number].x > customers[equalDistanceNumber].x:
            number = equalDistanceNumber
        elif customers[number].x == customers[equalDistanceNumber].x:   # 행이 같다면 열이 더 작은 손님 선택
            if customers[number].y > customers[equalDistanceNumber].y:
                number = equalDistanceNumber
    taxi.x = customers[number].goalX    # 택시를 손님 목적지로 이동
    taxi.y = customers[number].goalY    # 택시를 손님 목적지로 이동
    visited[number] = True  # 손님 방문 표시
    return number, distance


def solution():
    road = []
    customers = []

    N, M, fuel = map(int, input().split())

    visited = [False] * M

    for _ in range(N):
        road.append(list(map(int, input().split())))

    taxi = Taxi(*map(int, input().split()))

    for i in range(M):
        x, y, goalX, goalY = map(int, input().split())
        customers.append(Customer(i, N, x, y, goalX, goalY, deepcopy(road)))
        if customers[i].distance is None:   # 만약 손님이 목적지까지 갈 수 없는 경우 종료
            return -1

    while False in visited:
        current, distance = findCustomer(N, taxi, customers, visited, deepcopy(road))   # 손님 찾기
        if current == distance == -1:
            return -1
        fuel -= distance    # 손님태우러 가는 연료
        fuel -= customers[current].distance # 목적지 까지 가는 연료
        if fuel < 0:    # 만약 목적지에 가다 연료가 부족하면 종료
            return -1
        fuel += customers[current].distance * 2 # 목적지 도착했을 때 주유

    return fuel


print(solution())
