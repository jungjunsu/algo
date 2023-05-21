T = int(input())

for i in range(1, T+1):
    input_str = input()
    count = 0
    for j in range(len(input_str)):
        if input_str[j] == 'o':
            count += 1
    if count >= 8 or count + (15 - len(input_str)) >= 8:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")