N = int(input())
ans_arr = []

if N < 1 or N > 1000:
    exit(1)
for i in range(1, N + 1):
    if N % i == 0:
        ans_arr.append(f"{i}")
print(" ".join(ans_arr))