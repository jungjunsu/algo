T = int(input())

def check_pattern(str, index):
    for i in range(index):
        if str[i] != str[i + index]:
            return False
    return True

for i in range(1, T+1):
    input_str = input()
    str_len = len(input_str)
    if str_len != 30:
        exit(1)
    for j in range(1, str_len):
        if input_str[0] == input_str[j]:
            if check_pattern(input_str, j):
                break

    print(f"#{i} {j}")