def solution():
    N, M = map(int, input().split())
    words = []
    cnt = 0
    for i in range(N):
        words.append(input())
        cnt += len(words[i])

    total_require = M - cnt  # 총 필요한 _의 수
    avg_require, require = divmod(total_require, (N-1)) # 평균 _ 의 수, 추가로 필요한 _의 수
    answer = words[0]
    for i in range(1, N):
        if words[i][0].islower() and require > 0:   # 소문자면 _ 추가해야함
            # 단, 필요한 _의 수가 남아 있을 경우에만 추가
            require -= 1
            answer += '_' * (avg_require + 1) + words[i]
        elif N - i == require:  # 남은 단어와 필요한 _의 수가 같다면 무조건 _를 추가해야함
            require -= 1
            answer += '_' * (avg_require + 1) + words[i]
        else:
            answer += '_' * avg_require + words[i]

    print(answer)
    return


solution()
