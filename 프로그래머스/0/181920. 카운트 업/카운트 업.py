def solution(start_num, end_num):
    a=[]
    for start_num in range(start_num, end_num+1):
        a.append(start_num)
        start_num = start_num+1
    return a