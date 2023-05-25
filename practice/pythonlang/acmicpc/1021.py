N, M = list(map(int, input().split()))
N_list = [e for e in range(1, N + 1)]
M_list = list(map(int, input().split()))
count = 0
for i in range(M):
    f_num = N_list.index(M_list[i])
    b_num = abs(N_list.index(M_list[i]) - N_list.index(N_list[-1]))
    if f_num <= b_num:
        for _ in range(f_num):
            count += 1
            N_list.append(N_list.pop(0))
        N_list.pop(0)
    else:
        for _ in range(b_num + 1):
            count += 1
            N_list.insert(0, N_list[-1])
            N_list.pop(-1)
        N_list.pop(0)
print(count)