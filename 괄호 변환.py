# (()())()실행 오류 수정필요
def solution(p):
    answer = ''
    n = len(p)
    while True:
        u, p = balance(p)
        u = "".join(u)
        p = "".join(p)
        answer += correctString(u)
        if len(answer) == n:
            break
    return answer

def balance(s):
    Lcnt = 0
    Rcnt = 0

    u = list()
    v = list()
    for i in s:
        if i == '(':
            Lcnt += 1
        else:
            Rcnt += 1
        u.append(i)
        if Lcnt == Rcnt:
            break
    v.append(s[len(u):])
    return u, v

def correctString(u):
    n = len(u)
    newU = ('('*(int(n/2)) + (')'*int(n/2)))
    return newU

print(solution('(()())()'))