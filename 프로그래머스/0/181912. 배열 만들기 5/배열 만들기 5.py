def solution(intStrs, k, s, l):
    x = []
    num = []
    for i in range(len(intStrs)):
        x.append(int(intStrs[i][s:s+l]))
        if x[i] > k:
            num.append(x[i])
    return num