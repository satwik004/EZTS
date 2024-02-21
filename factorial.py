'''
def factorial(n):
	res = 1
	for i in range(2, n+1):
		res *= i
	return res
num = int(input())
print(factorial(num))
'''
def factorial(n):
  if(n == 0 or n == 1):
    return 1
  else:
   return (n * factorial(n-1))
num = int(input())
print(factorial(num))


