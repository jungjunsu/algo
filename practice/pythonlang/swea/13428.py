T = int(input())

for i in range(1, T+1):
    N = int(input())
    N_list = list(str(N))
    N_len = len(str(N))
    max = 0
    min = N
    current_val = 0
    for a in range(N_len):
        for b in range(a, N_len):
            temp_list = list(str(N))
            if a == 0 and temp_list[b] == "0":
                pass
            else:
                temp_list[a], temp_list[b] = temp_list[b], temp_list[a]
            current_val = int("".join(temp_list))
            if max < current_val:
                max = current_val
            if min > current_val:
                min = current_val
    print(f"#{i} {min} {max}")