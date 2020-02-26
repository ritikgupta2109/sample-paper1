n=int(input())
a=[]
for i in range(n):
	a.append(int(input()))
b=[]
for i in a:
	if i!=0:
		b.append(i)
c=n-len(b)
for i in range(c):
	b.append(0)
print(b)


