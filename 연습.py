from datetime import date, timedelta
import random

id = 0  # 게스트 아이디


class Room:
    def __init__(self, id, price):  # Room 생성자
        self.id = id  # 방번호
        self.price_per_day = price  # 방가격
        self.guest = None  # 게스트

    def CheckInGuest(self, guest):  # 게스트 체크인
        self.guest = guest

    def showInfo(self):  # 출력
        if self.guest == None:
            print('\tRoom {0}(Empty)'.format(str(self.id)))
        else:
            print('\tRoom {0}(Geust #{1} {2}) checkout: {3}'.format(self.id, self.guest.id, self.guest.name,
                                                                    self.guest.checkOutDate))

    def checkOutInfo(self):  # 체크아웃 정보 출력
        print("\t'room_no': {0}, 'guest_name': '{1}', 'days': {2}, 'payment': {3}".format(self.id, self.guest.name,
                                                                                          self.guest.day, (
                                                                                                      self.price_per_day * self.guest.day)),
              end="")

    def checkRoom(self):  # 방이 비었는지 확인, 비었으면 True, 아니면 False
        if self.guest == None:
            return True
        else:
            return False


class Guest:
    def __init__(self, today):  # Guest 생성자
        global id  # 전역변수 사용
        self.id = id  # 게스트 아이디
        id += 1  # 아이디 인덱스 증가
        self.name = random.choice(name)  # 게스트 이름
        self.day = random.randint(1, 4)  # 숙박기간
        self.checkInDate = today  # 체크인 날짜
        self.checkOutDate = today + timedelta(days=self.day)  # 체크아웃 날짜
        self.room = False  # 투숙했는지 여부


roomNumber = 100  # 방 인덱스
today = date.today()  # 오늘 날짜
price = [100000, 80000, 60000, 40000]  # 방 가격 리스트
name = ['김', '이', '박', '최', '남궁', '장', '정', '신']  # 게스트 이름 리스트
rooms = [Room(roomNumber + i, random.choice(price)) for i in range(5)]  # 5개의 방 생성
guests = []  # 게스트 리스트

day = 1

while (True):
    print('DATE:')  # 오늘 날짜 출력
    print(today.strftime('%Y-%m-%d'))

    guests.append(Guest(today))  # 게스트 추가
    for i in rooms:
        if i.checkRoom():  # 방이 비어있으면
            i.CheckInGuest(guests[-1])  # 최근 손님 체크인
            guests[-1].room = True  # 투숙 여부 True
            todayRoom = i
            break

    cnt = 0
    for i in rooms:
        if i.checkRoom() == False:
            if i.guest.checkOutDate == today:
                cnt += 1
    print('\n{0} CHECK-OUT RECEIPTS:'.format(cnt))  # 오늘 체트아웃 출력
    for i in rooms:
        if i.checkRoom() == False:
            if i.guest.checkOutDate == today:
                print('{', end="")
                i.checkOutInfo()
                print('}')

    # 오늘 체크인 출력
    if guests[-1].room:  # 체크인 성공시
        print('\nCHECK-IN:')
        todayRoom.showInfo()
    else:  # 체트인 실패시
        print('\nCHECK_IN failed:')
        print('\tGuest #{0} {1}'.format(guests[-1].id, guests[-1].name))

    # 전체 방 정보 출력
    print('\nROOMS:')
    for i in rooms:
        i.showInfo()

    # 체크아웃
    for i in rooms:
        if i.checkRoom() == False:
            if i.guest.checkOutDate == today:
                i.guest = None

    today = today + timedelta(days=day)  # 날짜 다음날로 변경

    input("\n\nPress <Enter> to continue...")
