
a = list(range(1,101))
for i in a:
	while i % 7==0 or (i//10)-7==0 or (i-7)%10==0:
		break
	else:
		print(i)
