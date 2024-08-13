# Method-1

n= int(input("Enter your number: "))
product=1
for i in range(1,n+1):
 product= product * i
print(f"The Factorial of {n} is {product}")

# Method-2

def factorial(n):
 if(n==1 or n==0):
  return 1
 return n * factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")
