testcase_num = int(input())
ans_arr = []

for i in range(testcase_num):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a < 1 or b < 1 or a > 10000 or b > 10000:
        exit(1)
    ans_arr.append(a // b)
    ans_arr.append(a % b)

for i in range(0, testcase_num * 2, 2):
    print(f"#{i // 2 + 1} {ans_arr[i]} {ans_arr[i+1]}")