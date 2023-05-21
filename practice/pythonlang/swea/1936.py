A, B = input().split()
A, B = int(A), int(B)
result_val = A - B

if result_val != -2 and result_val < 0:
    print("B")
else:
    print("A")