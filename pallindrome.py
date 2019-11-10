def isPalindrome(n):
	num = n
	d = 0
	rev = 0
	while n>0:
		d = n%10
		n = int(n/10)
		rev = rev*10+d

	if num==rev:
		return True
	else:		
		return False	
x = int(input("Enter a number : "))
if isPalindrome(x):
	print(x,"is Palindrome")
else:
	print(x,"is not Palindrome")
