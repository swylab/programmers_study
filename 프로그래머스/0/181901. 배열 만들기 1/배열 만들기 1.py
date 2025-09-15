def solution(n, k):
    answer = []
    i=1
    for i in range(1,n+1):
        if i%k == 0:
            answer.append(i)
    return answer