def solution(s):
    n = len(s)//2
    newString = ""
    answer = s

    for j in range(1, n+1):
        cnt = 1
        i = 0
        newString = ""
        while True:
            word = s[i:i+j]
            if i >= len(s):
               break
            if s[i:i+j] == s[i+j:i+j*2]:
                cnt += 1
                i = i+j
                if i+j > len(s):
                    newString += (str(cnt) + s[i - j:i])
                    newString += (s[i+j*2:])
                    break
            else:
                if cnt > 1:
                    newString += (str(cnt) + s[i-j:i])
                    cnt = 1
                else:
                    newString += s[i:i+j]
                i += j

        if len(newString) < len(answer) and len(answer) != 0:
            answer = newString[:]
    return len(answer)
