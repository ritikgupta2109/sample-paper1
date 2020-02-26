a=list(map(int,input().split()))
b=[]
for i in range(1,101):
	if i not in a:
		b.append(i)
print(b)
	
