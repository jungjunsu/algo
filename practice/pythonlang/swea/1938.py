a, b = input().split()
a, b = int(a), int(b)
ans_arr = []

if (a < 1) or (b > 9) or b == 0:
    exit(1)
ans_arr.append(a+b)
ans_arr.append(a-b)
ans_arr.append(a*b)
ans_arr.append(a//b)
for i in range(len(ans_arr)):
    print(ans_arr[i])