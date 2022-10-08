n = int(input())
cnt = 1
while cnt*(cnt+1)<n*2:
    cnt += 1
cnt -= 1
if (cnt+1) % 2 == 0:
    r = 1
    l = cnt+1
else:
    r = cnt+1
    l = 1
x = int(n - cnt*(cnt+1)/2)-1
for _ in range(x):
    if r==1and l==1:
        break
    if (cnt+1) % 2 == 0:
        r += 1
        l -= 1
    else:
        r -= 1
        l += 1

result = str(r)+'/'+str(l)
print(result)