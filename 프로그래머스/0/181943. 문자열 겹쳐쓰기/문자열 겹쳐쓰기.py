def solution(m, o, s):
    answer=[]
    for i in range(len(m)):
        if i < s:
            answer.append(m[i])
        elif i >= s + len(o):
            answer.append(m[i])
        else:
            answer.append(o[i-s])
    a = "".join(answer)
    return a

        
