def solution(n, cl):
    for i in range(len(cl)):
        if cl[i] == "w":
            n = n+1
        elif cl[i] == "s":
            n = n-1
        elif cl[i] == "d":
            n = n+10
        elif cl[i] == "a":
            n = n-10
    return n