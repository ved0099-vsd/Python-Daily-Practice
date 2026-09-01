CP = float(input("Enter COST Price :"))
SP = float(input("Enter Selling Price :"))

if(CP > SP ):
    print("LOSS", CP-SP)

elif(SP > CP):
    print("PROFIT", SP - CP)

else:
    print("NO profit No LOSS")