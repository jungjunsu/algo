testcase_num = int(input())
ans_arr = []
temp_arr = []

for i in range(testcase_num):
    temp_arr = input().split()
    for j in temp_arr:
        if int(j) < 0 or int(j) > 10000:
            exit(1)
    sign = int(temp_arr[0]) - int(temp_arr[1])
    if sign > 0:
        ans_arr.append(">")
    elif sign < 0:
        ans_arr.append("<")
    else:
        ans_arr.append("=")

for i in range(testcase_num):
    print(f"#{i+1} {ans_arr[i]}")