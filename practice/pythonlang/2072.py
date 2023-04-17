t=int(input())
p=[0]*10
a=[0]*t
for i in range(t):
	p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]=input().split()
	for j in range(10):
		if (int(p[j])<0 or int(p[j])>10000):
			exit()
		elif (int(p[j])%2):
			a[i]+=int(p[j])
for k in range(t):
	print('#'+str(k+1)+' '+str(a[k]))
