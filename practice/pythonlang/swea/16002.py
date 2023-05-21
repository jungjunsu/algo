TC = int(input())

def check_comp(x, y):
    x_ok = 0
    y_ok = 0

    for i in range(2, x):
        if x % i == 0:
            x_ok = 1
            break
    for j in range(2, y):
        if y % j == 0:
            y_ok = 1
            break
    if x_ok and y_ok:
        return True

    return False

def check_range(x):
    if x > 10 ** 9:
        return False

    return True

for i in range(1, TC+1):
    N = int(input())
    x = N + 2

    while check_range(x):
        if check_comp(x, x - N):
            break
        x += 1

    print(f"#{i} {x} {x - N}")