d = list(map(int,input().split()))
c = 50
h = 30
for i in d:
	Q=((2*c*i)/h)**0.5
	print(Q,end=',')
