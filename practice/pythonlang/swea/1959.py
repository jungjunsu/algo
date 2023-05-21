T = int(input())

def comp_list(c_list, filter_list):
    max_val = 0
    curren_val = 0
    for i in range(len(filter_list) - len(c_list) + 1):
        curren_val = 0
        if (len(filter_list) == len(c_list)):
            i = 0
        for j in range(len(c_list)):
            curren_val += c_list[j] * filter_list[j + i]
        if max_val < curren_val:
            max_val = curren_val
    return max_val

for i in range(1, T+1):
    N, M = map(int, input().split())
    max_val = 0
    if N < 3 or M < 3 or N > 20 or M > 20:
        exit(1)
    N_list = list(map(int, input().split()))
    M_List = list(map(int, input().split()))
    if N != len(N_list) or M != len(M_List):
        exit(1)
    if N < M:
        max_val = comp_list(N_list, M_List)
    else:
        max_val = comp_list(M_List, N_list)

    print(f"#{i} {max_val}")