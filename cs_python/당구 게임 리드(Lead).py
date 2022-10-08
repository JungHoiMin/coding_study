player: int
lead = 0
n = int(input())
n1 = n2 = 0
for _ in range(n):
    a, b = map(int, input().split())
    n1 += a
    n2 += b
    score = n1 - n2 if n1 > n2 else n2 - n1
    if score > lead:
        lead = score
        player = 1 if n1 > n2 else 2

print(player, lead)

