print("-" * 40)
print("Number Range Checker")
print("-" * 40)

Num = int(input("Enter your Number"))

if Num > 0:
    if(Num <= 100):
        print("Number is between 1 and 100 ")
    else:
        print("Number is greater than 100 ")

else:
    print("No. is Negative")