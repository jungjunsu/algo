N = int(input())
i = 1
sum = 0

if N < 1 or N > 9999:
    exit(1)
while N - i > 0:
    i *= 10
i //= 10
while i > 0:
    sum += N // i
    N %= i
    i //= 10
print(sum)