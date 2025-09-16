def solution(my_string, is_prefix):
    all_prefix = []
    for i in range(len(my_string)):
        all_prefix.append(my_string[:i])
    if is_prefix in all_prefix:
        return 1
    else:
        return 0
