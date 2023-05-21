T = int(input())


def check_box(N_list, N):
    index = []
    box_exist = 0
    tc = 0
    if N == 1:
        if N_list[0][0] == "#":
            return True
    for t in range(N):
        for c in range(N):
            if N_list[t][c] == '#':
                tc += 1
    if tc == N * N:
        return True
    for row in range(N ):
        for col in range(N):
            if row - 1 >= 0 and col - 1 >= 0:
                if N_list[row - 1][col] == "#" or N_list[row][col - 1] == "#" or N_list[row - 1][col - 1] == "#":
                    break
            if N_list[row][col] == "#":
                index.append(row)
                index.append(col)
                box_exist = 1
    if box_exist == 0:
        return False
    for i in range(0, len(index), 2):
        k = index[i]
        size = 0
        while k < N:
            if N_list[k][index[i + 1]] == ".":
                break
            size += 1
            k += 1
        if index[i] + size - 1 >= N or index[i + 1] + size - 1 >= N:
            continue
        else:
            for a in range(index[i], index[i] + size):
                count = 0
                for b in range(index[i + 1] - 1, 0, -1):
                    if N_list[a][b] != '#':
                        break
                    count += 1
                for c in range(index[i + 1] + 1, N, +1):
                    if N_list[a][c] != '#':
                        break
                    count += 1
                if count != size - 1:
                    return False

            for d in range(index[i + 1], index[i + 1] + size):
                count = 0
                for e in range(index[i] - 1, 0, -1):
                    if N_list[e][d] != '#':
                        break
                    count += 1
                for f in range(index[i] + 1, N, +1):
                    if N_list[f][d] != '#':
                        break
                    count += 1
                if count != size - 1:
                    return False
    if tc != size*size:
        return False
    return True


for i in range(1, T + 1):
    N = int(input())
    N_list = [["" for col in range(N)] for row in range(N)]
    for row in range(N):
        N_list[row] = list(input())
    if check_box(N_list, N):
        print(f"#{i} yes")
    else:
        print(f"#{i} no")