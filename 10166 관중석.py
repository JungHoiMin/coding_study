from sys import stdin
from math import gcd
# def gcd(a: int, b: int):
#     while True:
#         r = a % b
#         if r == 0:
#             break
#         a = b
#         b = r
#     return b


D1, D2 = map(int, stdin.readline().split())
answer = 0
save = [[0] * (D2+1) for _ in range(D2+1)]
for i in range(D1, D2 + 1):
    for j in range(1, i + 1):
        g = gcd(i, j)
        div_parent, div_son = i // g, j // g
        if not save[div_parent][div_son]:
            save[div_parent][div_son] = 1
            answer += 1

print(answer)
