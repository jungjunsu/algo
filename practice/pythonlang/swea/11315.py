T = int(input())

def check_vertical(input_list, N):
    for col in range(N):
        count = 0
        for row in range(N):
            if input_list[row][col] == 'o':
                count += 1
            else:
                count = 0
            if count >= 5:
                return True
    return False

def check_horizontal(input_list, N):
    for row in range(N):
        count = 0
        for col in range(N):
            if input_list[row][col] == 'o':
                count += 1
            else:
                count = 0
            if count >= 5:
                return True
    return False

def check_diagonal(input_list, N):
    for row in range(N):
        for col in range(N):
            count = 0
            if row + 4 < N and (col + 4 < N or col - 4 >= 0):
                for i in range(5):
                    j = i
                    if col - 4 >= 0:
                        j = -i
                    if input_list[row + i][col + j] == 'o':
                        count += 1
            if count == 5:
                return True
    return False

for i in range(1, T+1):
    N = int(input())
    input_list = [['' for col in range(N)] for row in range(N)]
    for row in range(N):
        input_list[row] = list(input())
    if check_vertical(input_list, N) or check_horizontal(input_list, N) or check_diagonal(input_list, N):
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")