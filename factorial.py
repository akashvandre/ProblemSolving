number = int(input("Enter a number: "))

def fact(number):
	if number == 0 or number==1:
		return 1
	else:
		return number*fact(number-1)

factorial=fact(number)
print("Factorial is {}".format(factorial))