# Procedural Programming - Lab 4, Part B: Vending Machine

# Stage 3 & 4: balance is set BEFORE the loop so it doesn't reset
balance = 200
running = True

print("Welcome to the Vending Machine!")
print("Your balance is " + str(balance) + "p.")

while running:
    # Stage 1: display the menu
    print("1. Crisps - 100p")
    print("2. Chocolate - 150p")
    print("3. Water - 120p")
    print("4. Quit")
    choice = int(input("Please select an option: "))

    # Stage 2: respond to the customer's choice
    if choice == 1:
        print("You selected Crisps. Price: 100p.")
        if balance >= 100:
            balance = balance - 100
            print("Purchase successful!")
            print("Remaining balance: " + str(balance) + "p.")
        else:
            print("Insufficient funds. Please choose a cheaper product.")

    elif choice == 2:
        print("You selected Chocolate. Price: 150p.")
        if balance >= 150:
            balance = balance - 150
            print("Purchase successful!")
            print("Remaining balance: " + str(balance) + "p.")
        else:
            print("Insufficient funds. Please choose a cheaper product.")

    elif choice == 3:
        print("You selected Water. Price: 120p.")
        if balance >= 120:
            balance = balance - 120
            print("Purchase successful!")
            print("Remaining balance: " + str(balance) + "p.")
        else:
            print("Insufficient funds. Please choose a cheaper product.")

    elif choice == 4:
        print("Thank you for using the vending machine!")
        running = False

    else:
        print("Invalid selection. Please try again.")
