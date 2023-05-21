import math

T = int(input())
ans_str = ""
prime_arr = []

def is_prime(t):
    for p in range(2, int(math.sqrt(t))):
        if int(t/p) == t/p:
            return False
    return True

for t in range(2, int(math.sqrt(10**7))):
    if t % 2 == 1:
        if is_prime(t):
            prime_arr.append(t)

for i in range(1, T+1):
    A = int(input())
    B = 1
    while math.sqrt(A*B) % 1 != 0:
        f = 1
        B += 1
        while not (A*B)%10 in [0, 1, 4, 5, 6, 9]:
            B += 1
            if B in prime_arr:
                B += 1
    ans_str += f"#{i} {B}\n"
print(ans_str.rstrip())