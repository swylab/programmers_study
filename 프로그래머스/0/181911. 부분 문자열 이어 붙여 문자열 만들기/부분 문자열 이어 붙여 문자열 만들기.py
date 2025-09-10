def solution(m, p):
    t=""
    for i in range(len(m)):
        t += m[i][p[i][0]:p[i][1]+1]
    return t
               
