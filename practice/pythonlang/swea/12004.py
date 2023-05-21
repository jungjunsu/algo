TC = int(input())

def check_num(N):
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                return True
    return False

for i in range(1, TC+1):
    N = int(input())
    if check_num(N):
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")