TC = int(input())

def check_pos(n_list, row, col):
    for i in range(col):
        if n_list[i] == row:
            return False
        if n_list[i] == row - (col - i) or n_list[i] == row + (col - i):
            return False
    return True

def queen_recursion():
    global depth_v
    global N_list
    global n_len
    global count

    depth_v += 1
    if depth_v == n_len:
        count += 1
        return -1
    for row in range(n_len):
        if check_pos(N_list, row, depth_v):
            N_list[depth_v] = row
            queen_recursion()
            depth_v -= 1
            N_list[depth_v] = 0

    return count

for tc in range(1, TC+1):
    N = int(input())
    N_list = [0 for _ in range(N)]
    depth_v = -1
    n_len = N
    count = 0
    count = queen_recursion()
    print(f"#{tc} {count}")
