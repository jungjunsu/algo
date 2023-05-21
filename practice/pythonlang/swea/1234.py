for tc in range(1, 10 + 1):
    N, N_list = list(map(int, input().split()))
    N_list = list(str(N_list))
    index = 0
    while index < len(N_list) - 1:
        if N_list[index] == N_list[index+1]:
            N_list.pop(index)
            N_list.pop(index)
            index += -2
        index += 1
    print(f"#{tc} {int(''.join(N_list))}")