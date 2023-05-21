for i in range(1,10+1):
    N = int(input())
    input_list = [['' for col in range(8)] for row in range(8)]
    count = 0
    for row in range(8):
        input_list[row] = list(input())
    for a in range(8):
        for b in range(8):
            for l in range(b+1, 8):
                if input_list[a][b] == input_list[a][l]:
                    line = 0
                    for k in range(0, l-b + 1, +1):
                        if input_list[a][b+k] == input_list[a][l-k]:
                            line += 1
                    if line == l - b + 1 and line == N:
                        count += 1
    for c in range(8):
        for d in range(8):
            for m in range(d+1, 8):
                if input_list[d][c] == input_list[m][c]:
                    line = 0
                    for q in range(0, m-d + 1, +1):
                        if input_list[d+q][c] == input_list[m-q][c]:
                            line += 1
                    if line == m - d + 1 and line == N:
                        count += 1
    print(f"#{i} {count}")