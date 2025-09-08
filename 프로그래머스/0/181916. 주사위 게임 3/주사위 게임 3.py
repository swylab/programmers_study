def solution(a, b, c, d):
    x = [a,b,c,d]
    # 모두 같다면 
    if a==b==c==d:
        answer=a*1111
        
    # 세개가 같다면
    elif a==c==d and a!=b:
        answer=(10*a+b)**2
    elif a==b==d and a!=c:
        answer=(10*a+c)**2
    elif a==b==c and a!=d:
        answer=(10*a+d)**2
    elif b==c==d and a!=b:
        answer=(10*b+a)**2
    
    # 두개/두개
    elif a==b and c==d:
        answer=(a+c)*abs(a-c)
    elif a==c and b==d:
        answer=(a+b)*abs(a-b)
    elif a==d and b==c:
        answer=(a+b)*abs(a-b)
    
    # 두개/한개/한개
    elif a==b and c!=d:
        answer=c*d
    elif a==c and b!=d:
        answer=b*d
    elif a==d and b!=c:
        answer=b*c
    elif b==c and a!=d:
        answer=a*d
    elif b==d and a!=c:
        answer=a*c
    elif c==d and a!=b:
        answer=a*b
        
    # 다 다름
    elif a!=b!=c!=d:
        answer=min(x)
        
    return answer