class Arithmetic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Multi(self):
        ans = self.No1 * self.No2
        return ans

    def Div(self):
        ans = self.No1 / self.No2
        return ans

Value1 = float(input("Enter first number : "))
Value2 = float(input("Enter second number : "))

Aobj = Arithmetic(Value1,Value2)

Ret = Aobj.Multi()
print("Multiplication is :",Ret)

Ret = Aobj.Div()
print("Division is :",Ret)