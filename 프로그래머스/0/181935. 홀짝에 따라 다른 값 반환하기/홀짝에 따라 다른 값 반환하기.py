def solution(n):
    i = 0
    sum = 0
    #홀수
    if n%2 == 1:
        for i in range(1, n+1):
            if i%2 == 1:
                sum = sum + i
        return sum
    #짝수
    else :
        for i in range(1, n+1):
            if i%2 == 0:
                sum = sum + i**2
        return sum
        
            
            
            
        
    answer = 0
    return answer