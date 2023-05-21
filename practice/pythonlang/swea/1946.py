T = int(input())
comp_list = []
origin_txt = ""

for i in range(1,T+1):
    N = int(input())
    origin_txt = ""
    comp_list = []
    count = 0
    if N < 1 or N > 10:
        exit(1)
    for j in range(N):
        comp_list += input().split()
    for k in range(0, len(comp_list), 2):
        for l in range(int(comp_list[k+1])):
            count += 1
            origin_txt += comp_list[k]
            if count >= 10:
                origin_txt += "\n"
                count = 0
    print(f"#{i}\n{origin_txt}")