class LL:
    def __init__(self, n):
        self.n = n
        self.checked = False
        self.prev = []
        self.next = None

    def enter_room(self, check: list):
        self.checked = True
        self.next = checkNextRoom(check, self.n + 1)
        check[self.next].prev.append(self.n)
        if not self.prev is None:
            check[self.next].prev.extend(self.prev)
            for room in check[self.next].prev:
                check[room].next = self.next


def checkNextRoom(check: list, room_number: int) -> int:
    if not check[room_number].checked:
        return room_number
    else:
        return checkNextRoom(check, check[room_number].next)


def solution(k, room_number):
    answer = []
    check = [LL(i) for i in range(k + 1)]
    while room_number:
        wanted_room = room_number.pop(0)
        if not check[wanted_room].checked:  # 원하는 방이 비어있으면
            check[wanted_room].enter_room(check)
            answer.append(wanted_room)
        else:
            next_room = checkNextRoom(check, check[wanted_room].next)
            check[next_room].enter_room(check)
            answer.append(next_room)

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
