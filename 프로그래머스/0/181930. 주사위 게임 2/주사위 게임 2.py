def solution(a, b, c):
    #a,b,c 다 같음 : (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    if a==b and b==c:
        x = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
        return x
    
    #a,b,c 다 다름 : a+b+c
    elif a!=b and b!=c and c!=a:
        x = a+b+c
        return x

    #두 숫자 같고, 한 숫자 다름 : (a+b+c)*(a**2+b**2+c**2)
    elif a==b and b!=c :
        x = (a+b+c)*(a**2+b**2+c**2)
        return x
    elif a==c and c!=b :
        x = (a+b+c)*(a**2+b**2+c**2)
        return x
    elif b==c and c!=a :
        x = (a+b+c)*(a**2+b**2+c**2)
        return x
    