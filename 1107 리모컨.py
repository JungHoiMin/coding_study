UP = True
DOWN = False


# +,- 버튼을 사용해 누른 횟수를 구하는 함수
def pmBtn(current: int, target: int):
    return abs(current - target)


# 고장난 버튼을 피해 누를 수 있는 버튼을 찾는 함수
def findBtn(current: int, broken: set, updown: bool):
    if current in broken:
        if updown == UP:
            new_target = (current + 1) % 10
        else:
            new_target = (current - 1 + 10) % 10
        return findBtn(new_target, broken, updown)
    else:
        return current


def find(broken: set, updown: bool):
    if updown == UP:
        for i in range(10):
            if i in broken:
                continue
            return i
    else:
        for i in range(9, -1, -1):
            if i in broken:
                continue
            return i


def solution():
    current_channel = 100
    N = input()  # 원하는 채널
    length = len(N)  # 원하는 채널의 자릿 수

    M = int(input())  # 고장난 버튼 수
    if M == 0:
        return length
    if M == 10:
        input()
        return pmBtn(current_channel, int(N))

    bb = set(map(int, input().split()))  # 고장난 버튼

    can = ""
    result = 0
    for i, n in enumerate(N):
        if int(n) not in bb:
            can += n
            if can == "0":
                can = "0"
            continue
        upDigit = int(can + str(findBtn(int(n), bb, UP)) + str(find(bb, UP)) * (length - (i + 1)))
        downDigit = int(can + str(findBtn(int(n), bb, DOWN)) + str(find(bb, DOWN)) * (length - (i + 1)))
        result = min(pmBtn(upDigit, int(N)), pmBtn(downDigit, int(N)))
        break

    answer = min(pmBtn(current_channel, int(N)), result + length)
    return answer


print(solution())
