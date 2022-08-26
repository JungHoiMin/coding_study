import sys


# player: 플레이어 번호, y: 이동할 곳 위치
def move(player: str, y: str, coordinate: dict):
    coordinate[player] = y


# player: 플레이어 번호, x: 파밍 아이템 번호
def farming(player: str, x: str, coordinate: dict, inventory: dict) -> bool:
    CHEATING = False  # 부정행위 시 True 반환

    # 플레이어 현재위치(위치가 저장되있으면 dict에서 찾고 없으면 초기위치 1)
    player_location = coordinate[player] if player in coordinate else '1'

    # 아이템 파밍
    if player in inventory:
        inventory[player].append(x)
    else:
        inventory[player] = [x]

    # 부정행위 판별
    if player_location != x:
        CHEATING = True

    return CHEATING


# player: 플레이어 번호, a: 아이템1 번호, b: 아이템2 번호
def crafting(player: str, a: str, b: str, inventory: dict) -> bool:
    CHEATING = False  # 부정행위 시 True 반환

    if player in inventory:
        if a in inventory[player]:  # a가 있는지 확인
            inventory[player].remove(a)  # a는 조합으로 인해 삭제
        else:
            CHEATING = True  # a가 없으면 부정행위

        if b in inventory[player]:  # b가 있는지 확인
            inventory[player].remove(b)  # b는 조합으로 인해 삭제
        else:
            CHEATING = True  # b가 없으면 부정행위
    else:  # 인벤토리가 없으면 부정행위
        CHEATING = True

    return CHEATING


# player: 플레이어 번호, enemy: 공격 대상의 번호
def attack(player: str, enemy: str, coordinate: dict) -> bool:
    CHEATING = False  # 부정행위 시 True 반환

    # 플레이어 현재위치(위치가 저장되있으면 dict에서 찾고 없으면 초기위치 1)
    player_location = coordinate[player] if player in coordinate else '1'

    # 적의 현재위치(위치가 저장되있으면 dict에서 찾고 없으면 초기위치 1)
    enemy_location = coordinate[enemy] if enemy in coordinate else '1'

    # 부정행위 판별
    if player_location != enemy_location:
        CHEATING = True

    return CHEATING


def solution():
    T, N = map(int, sys.stdin.readline().split())  # T: 로그의 수, N: 플레이어의 수

    coordinate = dict()
    inventory = dict()

    cheating = []
    cnt_logs = 0
    blocking = set()
    cnt_blocks = 0

    for _ in range(T):
        log = list(sys.stdin.readline().split())
        line_number, player_number, action_code, action_argument1 = log[0], log[1], log[2], log[3]

        if action_code == 'M':
            move(player_number, action_argument1, coordinate)

        elif action_code == 'F':
            if farming(player_number, action_argument1, coordinate, inventory):
                cheating.append(line_number)
                cnt_logs += 1

        elif action_code == 'C':
            action_argument2 = log[4]
            if crafting(player_number, action_argument1, action_argument2, inventory):
                cheating.append(line_number)
                cnt_logs += 1

        elif action_code == 'A':
            if attack(player_number, action_argument1, coordinate):
                cheating.append(line_number)
                cnt_logs += 1
                if player_number not in blocking:
                    blocking.add(player_number)
                    cnt_blocks += 1

    print(cnt_logs)
    if cnt_logs:
        print(' '.join(cheating))

    print(cnt_blocks)
    if cnt_blocks:
        blocking = list(blocking)
        blocking.sort()
        print(' '.join(blocking))


if __name__ == "__main__":
    solution()
