T = int(input())
is_pos = 1

def check_line(sudoku):
    for i in range(9):
        for j in range(8):
            for k in range(1, 9-j):
                if sudoku[i][j] == sudoku[i][j+k]:
                    return False
    for i in range(9):
        for j in range(8):
            for k in range(1, 9-j):
                if sudoku[j][i] == sudoku[j+k][i]:
                    return False
    return True

def check_area(sudoku):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sum1 = 0
            sum2 = 1
            for a in range(3):
                for b in range(3):
                    sum1 += sudoku[i+a][j+b]
                    sum2 *= sudoku[i+a][j+b]
            if sum1 != 45 or sum2 != 362880:
                return False
    return True

def check_correct(sudoku):
    if check_line(sudoku) and check_area(sudoku):
        return True
    return False

for i in range(1, T+1):
    sudoku_list = [[0 for c in range(9)] for r in range(9)]
    is_pos = 1
    for row in range(9):
        sudoku_list[row] = list(map(int, input().split()))
    if not check_correct(sudoku_list):
        is_pos = 0
    print(f"#{i} {is_pos}")