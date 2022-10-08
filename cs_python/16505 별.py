import copy


def copyStar(star: list):
    temp = copy.deepcopy(star)
    whitespace = [[" "] * len(star) for _ in range(len(star))]
    for i in range(len(star)):
        star[i].extend(temp[i][:])

    for i in range(len(temp)):
        temp[i].extend(whitespace[i])
    star.extend(temp)


def printStar(length: int):
    star = [['*', '*'], ['*', ' ']]
    for _ in range(2, length+1):
        copyStar(star)

    if length == 0:
        print("*")
        return

    starLength = pow(2, length)
    for line in star:
        for i in range(0, starLength):
            print(line[i], end="")
        starLength -= 1
        print()


if __name__ == "__main__":
    N = int(input())
    printStar(N)
