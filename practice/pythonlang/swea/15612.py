T = int(input())

def check_pos(chess_list):
    count = 0
    for row in range(8):
        count = 0
        for col in range(8):
            if chess_list[8 * row + col] == "O":
                count += 1
        if count != 1:
            return "no"

    for row in range(8):
        count = 0
        for col in range(8):
            if chess_list[8 * col + row] == "O":
                count += 1
        if count != 1:
            return "no"

    return "yes"

for i in range(1, T+1):
    chess_list = ""
    for j in range(8):
        chess_list += input()
    print(f"#{i} {check_pos(chess_list)}")