def solution(n):
    x = 0
    y = 0
    #홀수만 순서대로 이어 붙인수 + 짝수만 순서대로 이어 붙인 수 
    for i in range(len(n)):
        if n[i]%2 == 1:
            x = str(x) + str(n[i])
        elif n[i]%2 == 0:
            y = str(y) + str(n[i])
    a = int(x) + int(y)
    return a
            
    