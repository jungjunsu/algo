T = int(input())

for i in range(1, T+1):
    input_str = input()
    str_len = len(input_str)
    count = 0
    if (input_str[0] == "("):
        count += 1
    for j in range(1, str_len - 1):
        if (input_str[j] == "("):
            count += 1
        if not (input_str[j - 1] == "(") and (input_str[j] == ")"):
            count += 1
    if not (input_str[str_len - 2] == "(") and (input_str[str_len - 1] == ")"):
        count += 1
    print(f"#{i} {count}")