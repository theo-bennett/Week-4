# Lab 4 - Exercise 4: Numbers Divisible by 6

divisible_by_6 = []
for number in range(0, 100):
    if number % 6 == 0:
        divisible_by_6.append(number)
print(divisible_by_6)
