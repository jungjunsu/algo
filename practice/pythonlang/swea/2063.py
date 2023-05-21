N = int(input())
arr = []

if not N % 2 or N < 9 or N > 200:
    exit(1)
arr = input().split()
for i in range(N):
    arr[i] = int(arr[i])
arr.sort()
print(arr[N//2])