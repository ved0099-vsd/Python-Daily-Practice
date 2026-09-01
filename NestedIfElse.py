print("-" * 30)
print("We will find out  largest of three numbers using Nested IF ELSE")
print("-" * 30)

No1 = int(input("Enter your Num 1  : "))
No2 = int(input("Enter your Num 2  : "))
No3 = int(input("Enter your Num 3  :" ))\

if (No1 > No2 and No1 > No3):
    print(No1,"Is largest")

elif(No2 > No1 and No2 > No3):
    print(No2,"Is largest")


else:
    print(No3,"Is largest")
