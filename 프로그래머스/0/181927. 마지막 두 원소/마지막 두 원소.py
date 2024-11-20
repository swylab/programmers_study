def solution(n):
    # 원소1 < 원소2 : return 원소2-원소1
    # 원소1 > 원소2 : return 2*원소2
    a = n
    x = len(n)-1
    if n[x] > n[x-1]:
        a.append(n[x]-n[x-1])
    else:
        a.append(n[x]*2)
    return a