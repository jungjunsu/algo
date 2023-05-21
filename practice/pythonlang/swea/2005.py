T = int(input())
ans_str = ""

for i in range(1, T+1):
    N = int(input())
    N_list = [[0 for c in range(N)] for r in range(N)]
    ans_str = ""
    if N < 1 or N > 10:
        exit(1)
    N_list[0][0] = 1
    for j in range(1, N):
        N_list[j][0] = 1
        N_list[j][j] = 1
        for k in range(1, j):
            N_list[j][k] = N_list[j-1][k] + N_list[j-1][k-1]
    for r in range(N):
        for c in range(N):
            if N_list[r][c] == 0:
                continue
            ans_str += str(N_list[r][c]) + " "
        ans_str.rstrip()
        ans_str += "\n"
    print(f"#{i}\n{ans_str.rstrip()}")