def solution(myString):
    answer = myString.split("x")
    answer = [x for x in answer if x]
    answer.sort()
    return answer