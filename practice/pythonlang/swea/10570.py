import math

TC = int(input())

def check_p(num):
    count = 0
    for i in range(int(len(num) // 2)):
        if num[i] == num[len(num) - 1 - i]:
            count += 1
    if count == len(num) // 2:
        return True
    return False

for i in range(1, TC+1):
    A, B = list(map(int, input().split()))
    count = 0
    for num in range(A, B + 1):
        p = 0
        rp = 0
        if math.sqrt(num) % 1 != 0:
            continue
        else:
            if check_p(str(int(math.sqrt(num)))):
                rp = 1
        if check_p(str(num)):
            p = 1
        if p and rp:
            count += 1
    print(f"#{i} {count}")