testcase_num = int(input())
ans_arr = []
temp_arr = []

for i in range(testcase_num):
    temp_arr = input().split()
    for j in range(len(temp_arr)):
        if not (temp_arr[j].isdigit()) or\
                int(temp_arr[j]) < 0 or int(temp_arr[j]) > 10000:
            exit(1)
        else:
            temp_arr[j] = int(temp_arr[j])
    ans_arr.append(max(temp_arr))


for i in range(testcase_num):
    print(f"#{i+1} {ans_arr[i]}")