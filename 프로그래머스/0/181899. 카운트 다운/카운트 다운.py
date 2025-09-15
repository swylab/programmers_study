def solution(start_num, end_num):
    answer = []
    i = end_num
    for i in range(start_num, end_num-1, -1):
        answer.append(i)

    return answer