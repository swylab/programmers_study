def solution(numLog):
    # w = +1
    # s = -1
    # d = +10
    # a = -10
    answer=''
    i = 1
    for i in range(1, len(numLog)):
        x = numLog[i] - numLog[i-1] 
        if x==1:
            answer= answer+"w"
        elif x==-1:
            answer= answer+"s"
        elif x==10:
            answer= answer+"d"
        elif x==-10:
            answer= answer+"a"
    return answer