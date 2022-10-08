def nextSave(select: tuple, direction: int, clockwise: bool, n: int, spiral: list):
    x, y = select
    if clockwise:
        TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3
    else:
        TOP, LEFT, BOTTOM, RIGHT = 0, 1, 2, 3

    current = spiral[x][y]
    for _ in range(4):
        if direction == TOP:
            selected = x - 1, y
        elif direction == BOTTOM:
            selected = x + 1, y
        elif direction == LEFT:
            selected = x, y - 1
        else:
            selected = x, y + 1

        if checkEmpty(selected, n, spiral):
            i, j = selected
            spiral[i][j] = current + 1
            return selected
        else:
            direction = (direction + 1) % 4

    return -1, -1


def checkEmpty(selected: tuple, n: int, spiral: list):
    x, y = selected
    if 0 <= x < n and 0 <= y < n:
        return spiral[x][y] == 0
    else:
        return False


def solution(n: int, clockwise: bool) -> list:
    if clockwise:
        TOP, RIGHT, BOTTOM, LEFT = 0, 1, 2, 3
    else:
        TOP, LEFT, BOTTOM, RIGHT = 0, 1, 2, 3

    answer = [[0 for _ in range(n)] for _ in range(n)]
    lt, rt, rb, lb = (0, 0), (0, n - 1), (n - 1, n - 1), (n - 1, 0)  # 좌상, 우상, 우하, 좌하 위치 저장
    answer[0][0], answer[0][n - 1], answer[n - 1][n - 1], answer[n - 1][0] = 1, 1, 1, 1
    while lt != rt != rb != lb:
        if clockwise:
            lt = nextSave(lt, RIGHT, clockwise, n, answer)
            rt = nextSave(rt, BOTTOM, clockwise, n, answer)
            rb = nextSave(rb, LEFT, clockwise, n, answer)
            lb = nextSave(lb, TOP, clockwise, n, answer)
        else:
            lt = nextSave(lt, BOTTOM, clockwise, n, answer)
            rt = nextSave(rt, LEFT, clockwise, n, answer)
            rb = nextSave(rb, TOP, clockwise, n, answer)
            lb = nextSave(lb, RIGHT, clockwise, n, answer)
    return answer


if __name__ == "__main__":
    for i in solution(5, True):
        print(i)
    print()
    for i in solution(6, False):
        print(i)
    print()
    for i in solution(9, False):
        print(i)
    print()

    print(solution(5, True) == [[1, 2, 3, 4, 1], [4, 5, 6, 5, 2], [3, 6, 7, 6, 3], [2, 5, 6, 5, 4], [1, 4, 3, 2, 1]])
    print(solution(6, False) == [[1, 5, 4, 3, 2, 1], [2, 6, 8, 7, 6, 5], [3, 7, 9, 9, 8, 4], [4, 8, 9, 9, 7, 3],
                                 [5, 6, 7, 8, 6, 2], [1, 2, 3, 4, 5, 1]])
    print(solution(9, False) == [[1, 8, 7, 6, 5, 4, 3, 2, 1], [2, 9, 14, 13, 12, 11, 10, 9, 8],
                                 [3, 10, 15, 18, 17, 16, 15, 14, 7], [4, 11, 16, 19, 20, 19, 18, 13, 6],
                                 [5, 12, 17, 20, 21, 20, 17, 12, 5], [6, 13, 18, 19, 20, 19, 16, 11, 4],
                                 [7, 14, 15, 16, 17, 18, 15, 10, 3], [8, 9, 10, 11, 12, 13, 14, 9, 2],
                                 [1, 2, 3, 4, 5, 6, 7, 8, 1]])
