#lambda

Add = lambda No1,No2 : No1 + No2
Sub = lambda No1,No2 : No1 - No2

Value1 = int(input("enter first number  :"))
Value2 = int(input("Enter second number :"))

Ret = Add(Value1,Value2)
print("Add is :",Ret)

Ret = Sub(Value1,Value2)
print("Sub is :",Ret)