C = int(input())
encoding_str = ["3211", "2221", "2122", "1411", "1132", "1231", "1114", "1312", "1213", "3112"]

for i in range(1, C+1):
    N, M = list(map(int, input().split()))
    N_list = []
    for row in range(N):
        N_list += list(map(int, input()))
    index = 0
    count = 0
    tmp = 0
    flags = 0
    sum_val = 0
    num_str = ""
    ans_list = []
    ans_str = ""
    if N_list[index] == 0:
        while (N_list[index] == 0):
            index += 1
    while (N_list[index + 55 - count]) != 1:
        count += 1
    num_str += str(count)
    for k in range(56 - count + 1):
        if N_list[index + k] == flags:
            num_str += str(tmp)
            flags = (flags + 1) % 2
            tmp = 0
        if len(num_str) == 4:
            ans_list.append(int(num_str))
            num_str = ""
        tmp += 1
    for l in range(8):
        ans_list[l] = encoding_str.index(str(ans_list[l]))
    for v in range(8):
        sum_val += ans_list[v] * (2 - 1 * (1 * (v % 2 == 1) - 1 * (v % 2 == 0)))
    if sum_val % 10:
        print(f"#{i} 0")
    else:
        print(f"#{i} {sum(ans_list)}")