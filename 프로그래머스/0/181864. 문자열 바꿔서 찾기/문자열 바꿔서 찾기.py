def solution(myString, pat):
    new_string = []
    list_String = list(myString)
    for i in range(len(list_String)):
        if list_String[i] == "A":
            new_string.append("B")
        else:
            new_string.append("A")
    new_string = ''.join(new_string)
    
    if pat in new_string: return 1
    else: return 0