def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorial(n-1)
num=int(input("Enter the number: "))
result=factorial(num)
print("factorial of {0} is {1}".format(num,result))
