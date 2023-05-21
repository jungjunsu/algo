input_val = int(input())
ans_val = 0

if input_val > 10000:
    exit(1)
ans_val = input_val * (input_val + 1) // 2
print(ans_val)