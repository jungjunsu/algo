T = int(input())

for i in range(1, T+1):
    input_str = list(input())
    for j in range(len(input_str)):
        if input_str[j] == "b":
            input_str[j] = "d"
        elif input_str[j] == "d":
            input_str[j] = "b"
        if input_str[j] == "p":
            input_str[j] = "q"
        elif input_str[j] == "q":
            input_str[j] = "p"
    print(f"#{i} {''.join(input_str)[::-1]}")