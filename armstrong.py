def isArmstrong(st):

	p = len(st)
	n = int(st)
	tot = 0
	num = n
	while(n>0):
		d = n%10
		tot = tot + (d**p)
		n = int(n/10)
	if(num == tot):
		return True
	else:
		return False
x =  input("Enter a number: ")
if isArmstrong(x):
	print(x,"is an Armstrong")
else:
	print(x,"is not Armstrong")