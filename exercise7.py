# Lab 4 - Exercise 7: Sum of Even Numbers Not Divisible by 3

total = 0
for number in range(0, 100):
    if number % 2 == 0 and number % 3 != 0:
        total = total + number
print(total)
