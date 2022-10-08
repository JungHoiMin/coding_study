# from collections import deque
#
#
# def calculate(postfix: deque):
#     stack = deque()
#     for ch in postfix:
#         if ch.isdigit():
#             stack.append(int(ch))
#         else:
#             n2 = stack.pop()
#             n1 = stack.pop()
#             if ch == '+':
#                 stack.append(n1 + n2)
#             elif ch == '-':
#                 stack.append(n1 - n2)
#             elif ch == '*':
#                 stack.append(n1 * n2)
#             else:
#                 stack.append(n1 // n2)
#     return stack.pop()
#
#
# def infix_to_postfix(infix: list[str]):
#     postfix = deque()
#     stack = deque()
#     digit = 0
#     digit_cnt, char_cnt = 0, 0
#     flag = False
#     for ch in infix:
#         if ch.isdigit():
#             digit_cnt += 1
#             digit = digit*10+int(ch)
#             flag = True
#         else:
#             if flag:
#                 postfix.append(str(digit))
#                 digit = 0
#                 flag = False
#             if ch in ['+', '-', '/', '*']:
#                 char_cnt += 1
#                 while stack and stack[-1] != '(' and getPriority(ch) <= getPriority(stack[-1]):
#                     postfix.append(stack.pop())
#                 stack.append(ch)
#             elif ch == '(':
#                 stack.append(ch)
#             elif ch == ')':
#                 op = stack.pop()
#                 while op != '(':
#                     postfix.append(op)
#                     op = stack.pop()
#     if flag:
#         postfix.append(str(digit))
#     while stack:
#         postfix.append(stack.pop())
#
#     if digit_cnt <= char_cnt:
#         return -1
#     else:
#         return postfix
#
#
# def getPriority(op: str):
#     if op in ['(', ')']:
#         return 2
#     elif op in ['*', '/']:
#         return 1
#     else:
#         return 0
#
#
# def solution():
#     try:
#         infix = list(input())
#         print(int(calculate(infix_to_postfix(infix))))
#     except:
#         print("ROCK")
#
#
# solution()
def solution():
    infix = input()
    test = ''
    if infix.count('()') != 0:
        answer = "ROCK"
    else:
        for c in infix:
            if c in ['(', ')'] or c.isdigit():
                test += c
            else:
                test += '&'
        infix = infix.replace('/', '//')
        try:
            eval(test)
            answer = int(eval(infix))
        except:
            answer = "ROCK"

    print(answer)


solution()
