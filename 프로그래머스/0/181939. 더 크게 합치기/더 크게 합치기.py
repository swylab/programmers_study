def solution(a, b):
    x = str(a) + str(b)
    y = str(b) + str(a)
    xx = int(x)
    yy = int(y)
    if xx >= yy:
        return xx
    elif xx < yy:
        return yy
