TC = int(input())

for i in range(1, TC+1):
    input_str = input().strip()
    N = int(input_str[0])
    N_list = list(input_str[2:].split())
    for k in range(0, 2*N, 2):
        N_list[k+1] = int(N_list[k+1])
    pos_a = 1
    pos_b = 1
    time_sum = N_list[1] - 1
    move_time = 0
    if N_list[0] == "B":
        pos_b = N_list[1]
    else:
        pos_a = N_list[1]
    for j in range(2, 2*N, 2):
        if N_list[j] == N_list[j-2]:
            if j == 2:
                time_sum = 0
                move_time = N_list[1] - 1
            move_time += abs(N_list[j+1] - N_list[j-1]) + 1
            time_sum += move_time
        else:
            if N_list[j] == "B":
                if move_time < abs(pos_b - N_list[j+1]):
                    time_sum += abs(pos_b - N_list[j+1]) - move_time
                else:
                    time_sum += 1
            else:
                if move_time < abs(pos_a - N_list[j+1]):
                    time_sum += abs(pos_a - N_list[j+1]) - move_time
                else:
                    time_sum += 1
            move_time = 0
        if N_list[j] == "B":
            pos_b = N_list[j+1]
        else:
            pos_a = N_list[j+1]
    print(f"#{i} {time_sum+1}")