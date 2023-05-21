T = int(input())
alpha_str = "abcdefghijklmnopqrstuvwxyz"

for i in range(1, T+1):
    input_str = input()
    count = 0
    for j in range(len(input_str)):
        if input_str[j] == alpha_str[j]:
            count += 1
        if input_str[j] != alpha_str[j]:
            break
    print(f"#{i} {count}")