def solution(binomial):
    answer = 0
    bi_list = binomial.split()
    if bi_list[1] == "+":
        answer = int(bi_list[0]) + int(bi_list[2])
    elif bi_list[1] == "-":
        answer = int(bi_list[0]) - int(bi_list[2])
    elif bi_list[1] == "*":
        answer = int(bi_list[0]) * int(bi_list[2])
        
    return answer