#Functional = Lambda

Add = lambda No1,No2 : No1 + No2
Sub = lambda No1,No2 : No1 - No2

Value1 = int(input("Enter first number : "))
Value2 = int(input("Enter second number : "))

Ret = Add(Value1,Value2)
print("Addition is ",Ret)

Ret = Sub(Value1,Value2)
print("Subtraction is ",Ret)