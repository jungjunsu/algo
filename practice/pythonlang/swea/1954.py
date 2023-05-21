T = int(input())
pattern_list = []
ans_list = []
print_str = ""
count = 0
sign = 0
row, col = 0, -1

for i in range(1, T+1):
    N = int(input())
    pattern_list = []
    ans_list = [[0 for c in range(N)] for r in range(N)]
    print_str = ""
    count = 0
    sign = 0
    row, col = 0, -1
    if N < 1 or N > 10:
        exit(1)
    if N == 1:
        print(f"#{1}\n1")
    else:
        pattern_list.append(N)
        for j in range(1, N):
            pattern_list += [N - j, N - j]
        for k in range(2*N-1):
            sign += 1
            while pattern_list[k] > 0:
                count += 1
                if sign % 4 == 1:
                    col += 1
                elif sign % 4 == 2:
                    row += 1
                elif sign % 4 == 3:
                    col -= 1
                else:
                    row -= 1 % N
                ans_list[row][col] = count
                pattern_list[k] -= 1
        print(f"#{i}")
        for k in range(N):
            print_str = ""
            for l in range(N):
                print_str += f"{ans_list[k][l]} "
            print(print_str.rstrip())