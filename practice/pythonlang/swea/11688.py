T = int(input())

for i in range(1, T+1):
    input_str = input().strip()
    a = 1
    b = 1
    for q in range(len(input_str)):
        if input_str[q] == "L":
            b += a
        else:
            a += b
    print(f"#{i} {a} {b}")