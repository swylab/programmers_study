def solution(myString):
    answer = []
    xlist = myString.split('x')
    for i in range(len(xlist)):
        answer.append(len(xlist[i]))
    return answer