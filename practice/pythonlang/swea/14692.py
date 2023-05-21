TC = int(input())

for i in range(1, TC+1):
    N = int(input())
    if (N - 1) % 2 == 1:
        print(f"#{i} Alice")
    else:
        print(f"#{i} Bob")