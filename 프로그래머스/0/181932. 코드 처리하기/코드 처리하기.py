def solution(code):
    mode = 0
    idx = 0
    ret = ""
    for idx in range(len(code)):
        # mode가 0일때
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            else:
                if idx%2 == 0:
                    ret=ret+code[idx]
        # mode가 1일때
        else:
            if code[idx] == "1":
                mode = 0
            else:
                if idx%2 == 1:
                    ret=ret+code[idx]
    if len(ret) == 0:
        return "EMPTY"
    return ret