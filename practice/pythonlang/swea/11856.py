TC = int(input())

for i in range(1, TC+1):
    S = list(input())
    count = 0
    while (len(S)):
        chr = S[0]
        while chr in S:
            S.remove(chr)
        count += 1
    if count == 2:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")