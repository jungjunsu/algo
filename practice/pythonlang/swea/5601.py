TC = int(input())

for i in range(1, TC+1):
    N = int(input())
    ans_str = ""
    for j in range(N):
        ans_str += f"1/{N} "
    print(f"#{i} {ans_str.rstrip()}")
