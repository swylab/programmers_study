def solution(n):
    x = 1
    y = 0
    # 원소의 곱 < 원소의 합**2 : return 1
    for i in range(len(n)):
        x = x * n[i]
        y = y + n[i]
    if x < y**2:
        return 1
    elif x > y**2:
        return 0