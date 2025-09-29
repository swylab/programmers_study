def solution(rny_string):
    new_list = []
    rny_list = list(rny_string)
    for i in range(len(rny_list)):
        if rny_list[i] == "m":
            new_list.append("rn")       
        else:
            new_list.append(rny_list[i])
    new_list = ''.join(new_list)
    return new_list