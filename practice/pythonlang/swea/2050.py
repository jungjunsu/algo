input_val = input()
ans_arr = []

if len(input_val) > 200:
    exit(1)
for i in input_val:
    ans_arr.append(str("ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(i) + 1))
print(" ".join(ans_arr))