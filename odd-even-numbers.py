# a) For loop: even numbers from 1 to 21
print("Even numbers from 1 to 21:")
for number in range(1, 22):
    if number % 2 == 0:
        print(number)

# b) While loop: odd numbers from 1 to 20
print("Odd numbers from 1 to 20:")
number = 1
while number <= 20:
    if number % 2 != 0:
        print(number)
    number += 1