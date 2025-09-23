def solution(num_list):
    answer_1 = 0
    answer_2 = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in range(len(num_list)):
            answer_2 *= num_list[i]
        return answer_2