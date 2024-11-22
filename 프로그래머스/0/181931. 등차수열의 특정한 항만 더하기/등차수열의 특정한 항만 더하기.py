def solution(a, d, inc):
    sum = 0
    for i in range(len(inc)):
        if inc[i] == 1:
            sum = sum + a+d*i
    print(sum)
    return sum