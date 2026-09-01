print("-" * 30)
print("ALPHABET,DIGIT,SPECIAL CHARACTER CHECKER")
print("-" * 30)


Checker = input("Enter a character: ")

if(Checker.isalpha()):
    print("Alphabet")

elif(Checker.isdigit()):
    print("DIGIT")

else:
    print("Special Char")
    
