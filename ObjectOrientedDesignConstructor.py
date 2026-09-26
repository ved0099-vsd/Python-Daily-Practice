#Input
#  ↓
#Constructor
#  ↓
#Object stores No1 and No2
#  ↓
#Methods use self.No1 and self.No2

class Arithmetic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans

    def Subs(self):
        Ans = self.No1 - self.No2
        return Ans

Value1 = int(input("Enter first number : "))
Value2 = int(input("Enter second numnber : "))

Aobj = Arithmetic(Value1,Value2)

Ret = Aobj.Addition()
print("Add is ",Ret)

Ret = Aobj.Subs()
print("Sub is :",Ret)
