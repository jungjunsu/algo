input_val = int(input())
ans_arr = []

if input_val > 30:
    exit(1)
for i in range(input_val + 1):
    ans_arr.append(f"{2 ** i}")
print(" ".join(ans_arr))