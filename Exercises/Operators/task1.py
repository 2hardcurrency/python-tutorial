# Write a Python program that calculates the sum and product of two numbers entered by the user.
# Write your program below

num = input("Enter two digit numbers: ").split()

a = int(num[0])
b = int(num[1])

sum = a + b
print("{} + {} = {}".format(a, b, sum(a, b)))
