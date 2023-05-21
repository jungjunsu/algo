P, K = input().split()
ans = 0

if int(P) < 0 or int(P) > 999:
    exit(1)
ans = int(P) - int(K) + 1
print(ans)