import sys

string = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

answer = ['_']*len(string)

idx = 0
word_len = len(word)
for i in range(len(string)):
    answer[idx] = string[i]
    idx += 1
    if string[i] == word[-1] and ''.join(answer[idx-word_len:idx]) == word:
        idx -= word_len

answer = ''.join(answer[:idx])
if answer == "":
    print("FRULA")
else:
    print(answer)
