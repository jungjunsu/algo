def gauss_elim(A,b):
	n = len(b)

	for i in range(n):
		current_row = i
		for j in range(i + 1,n):
			if (abs(A[j][i]) > abs(A[current_row][i])):
				current_row = j
		A[i], A[current_row] = A[current_row], A[i]
		b[i], b[current_row] = b[current_row], b[i]

		for j in range(i+1,n):
			diagonal_division = A[j][i] / A[i][i]
			for k in range(i,n):
				A[j][k] -= diagonal_division*A[i][k]
			b[j] += diagonal_division*b[i]

	for x, y, z in arr:
		print(x, y, z)

arr = [[-2,-5,2],[1,3,0],[0,1,3]]
b = [-3,4,6]

gauss_elim(arr,b)
