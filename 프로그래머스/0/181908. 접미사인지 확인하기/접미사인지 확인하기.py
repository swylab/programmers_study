def solution(my_string, is_suffix):
    answer = 0
    all_suffix = []
    for i in range(len(my_string)):
        all_suffix.append(my_string[i::])
    if is_suffix in all_suffix:
        return 1
    else:
        return 0
