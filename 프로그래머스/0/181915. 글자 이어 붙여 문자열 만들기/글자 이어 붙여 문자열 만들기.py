def solution(m, i):
    answer = ''
    for x in range(len(i)):
        answer += m[int(i[x])]
    return answer