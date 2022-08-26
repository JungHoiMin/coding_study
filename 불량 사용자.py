import re

def solution(user_id, banned_id):
    answer = 0
    users = ' '.join(user_id) + ' '
    print(users)
    for bid in banned_id:
        bid = bid.replace('*', ".") + '\s'
        m = re.findall(bid, users)
        if len(m) != 0:
            if answer == 0:
                answer = len(m)
            else:
                answer *= len(m)

    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
