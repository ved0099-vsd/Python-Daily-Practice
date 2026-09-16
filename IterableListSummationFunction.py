#Creates a function named Summation.

#List → Function → for loop → Summation → return → Ret

def Summation(Data):   #Data is the parameter. It will receive the list.
    Sum = 0            #Creates a variable Sum and starts it from 0.

    for no in Data:    #The loop takes every element from the list one by one.
        Sum = Sum + no    #Adds each value to Sum.

    return Sum       #Returns the final answer ___ from the function.
 
def main(): 
    Marks = [78,90,56,98,77] 
 
    Ret = Summation(Marks)   #Calls the function and sends Marks to Data.
 
    print("addition is : ",Ret) 
 
if __name__ == "__main__": 
    main()