print("Enter your Weight")
print("Enter your Height")

Weight = float(input())
Height = float(input())

if(Weight >= 80):
    print(Weight,"OverWeight")

elif(Weight >= 60):
    print(Weight,"Okay Weight")

elif(Weight >= 50):
    print(Weight,"Low Weight")

elif(Weight >= 25):
    print(Weight,"too much Underweight")

else:
    print("You are just a Stick")
