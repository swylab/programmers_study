def solution(m, s, e):
    if s == 0 and e == 0:
        return m[0:len(m)+1]
    elif s == 0:
        return m[e:0:-1] + m[0] + m[e+1:]
    else:
        return m[:s] + m[e:s-1:-1] + m[e+1:]