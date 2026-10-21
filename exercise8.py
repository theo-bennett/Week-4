# Lab 4 - Exercise 8: Factorial

n = int(input("Enter a positive integer: "))
factorial = 1
for number in range(1, n + 1):
    factorial = factorial * number
print("The factorial is", factorial)
