print("Enter first number")
No1 = int(input())

print("Enter second number")
No2 = int(input())

print("Enter third number")
No3 = int(input())

if(No1 <= No2 and No1 <= No3):
    print(No1,"is smallest")

elif(No2 <= No1 and No2 <= No3):
    print(No2, "Is smallest")

else:
    print(No3 ,"is smallest")