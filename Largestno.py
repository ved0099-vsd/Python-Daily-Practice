print("Enter first No.")
No1 = int(input())

print("Enter second No.")
No2 = int(input())

print("Enter third No.")
No3 = int(input())

if(No1 >= No2 and No1 >= No3 ):
    print(No1,"Is largest no.")

elif(No2 >= No1 and No2 >= No3 ):
    print(No2,"Is largest no.")

else:
    print("No3 is greater", No3)