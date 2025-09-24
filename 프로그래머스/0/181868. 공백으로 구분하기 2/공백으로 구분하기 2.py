def solution(my_string):
    answer = []
    name = my_string.split(" ")
    for i in range(len(name)):
        if name[i] != "":
            answer.append(name[i])
    return answer