N = int(input())
ans_str = ""

if N < 10 or N > 1000:
    exit(1)
for i in range(1, N+1):
    count = 0
    current_str = str(i)
    if "3" in current_str or "6" in current_str or "9" in current_str:
        for j in range(len(current_str)):
            if not int(current_str[j]) == 0 and int(current_str[j]) % 3 == 0:
                ans_str += "-"
    else:
        ans_str += current_str
    ans_str += " "
print(ans_str.rstrip())