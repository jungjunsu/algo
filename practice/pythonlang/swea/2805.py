T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = [[0 for _ in range(N)] for _ in range(N)]
    sum_val = 0
    seq_index = (N - 1) // 2
    for row in range(N):
        N_list[row] = list(map(int, input()))
    for row in range(N):
        s_index = abs(seq_index - row)
        for i in range(N - 2 * abs(seq_index - row)):
            sum_val += N_list[row][s_index + i]
    print(f"#{tc} {sum_val}")