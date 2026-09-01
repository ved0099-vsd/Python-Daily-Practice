print("Age Calculator")

print("enter 1st no.")
num1 = float(input())

print("enter 2nd no.")
num2 = float(input())

choice = int(input("enter your choice"))

if(choice == 1):
    print("1.Addition", num1 + num2)

elif(choice == 2):
    print("2.Subs", num1 - num2)

elif(choice == 3):
    print("3.Mult", num1 * num2)

elif(choice == 4):
    print("4.Div", num1 / num2)

    if num2 != 0:
        print("Answer =", num1 / num2)
    else:
        print("Division by zero is not allowed.")



else:
    print("invalid choice")
