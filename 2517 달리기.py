import sys


def BIT_sum(i: int) -> int:
    answer = 0
    while i > 0:
        answer += tree[i]
        i -= (i & -i)
    return answer


def BIT_update(i: int, num: int):
    while i <= N:
        tree[i] += num
        i += (i & -i)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    nums = []

    for i in range(N):
        current = int(sys.stdin.readline())
        nums.append([current, i + 1])  # [실력, index]를 저장 한다.
    nums.sort()  # 모든 입력 값을 받은 후 정렬 한다.

    # N은 3 이상 500,000 이하 이다. -- (1)
    # 각 정수는 1 이상 1,000,000,000 이하 이다. -- (2)
    # 단, 참가한 선수들의 평소 실력은 모두 다르다. -- (3)

    # (1) 조건과 (3)조건에 의해 (2) 조건을 각 정수는 1이상 500,000 이하 이다. 라고 변경할 수 있다.
    tree = [0] * (N + 3)
    for i in range(N):
        nums[i][0] = nums[i][1]
        nums[i][1] = i + 1
    nums.sort()  # 조건을 변경한 후 입력 받은 index 를 순서로 정렬 한다.

    for i in range(N):
        temp = nums[i][1]
        print((i + 1) - BIT_sum(temp - 1))  # BIT 합을 구해서 [현재 자신의 등수에서] [자신 보다 실력이 낮은 사람들의 수를] 뺀다.
        BIT_update(temp, 1)  # 자신을 BIT에 추가한다.
