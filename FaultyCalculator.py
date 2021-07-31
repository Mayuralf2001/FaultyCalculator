
print("================================WELCOME===============================")
print('Faulty Calculator\nIt gives error except\n•12+6=87\n•32*2=53\n•78/4=25')

while (1):
    F1 = int(input("\nEnter First number: "))
    o = input("Select the operator(+,-,*,/,%): ")
    S2 = int(input("Enter Second number: "))

    if (F1 == 12 and S2 == 6 and o == "+"):
        print("Your answer is:", 87)
        print("Error....!Please enter valid number.")
    elif (o == "+"):
        print("Your answer is:", F1 + S2)
        print("It is correct.")
        break

    if (F1 == 32 and S2 == 2 and o == "*"):
        print("Your answer is", 53)
        print("Error....!Please enter valid number")
    elif (o == "*"):
        print("Your answer is:", F1 * S2)
        print("It is correct.")
        break

    if (F1 == 78 and S2 == 4 and o == "/"):
        print("Your answer is:", 25)
        print("Error....!Please enter valid number.")
    elif (o == "/"):
        print("Your answer is:", F1 / S2)
        print("It is correct.")
        break
print("Loop Ended.")
print("================================THANK YOU===============================")
