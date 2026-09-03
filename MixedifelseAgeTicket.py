#Age & Ticket 🎟️

#Take the user's age.

#Below 5 → Free ticket
#5–17 → ₹50
#18–59 → ₹100
#60 or above → ₹70

#Print the ticket price.

def main():
    Age = int(input("Enter age : ")) #Because Python reads code from top to bottom, any age greater than 5 matches the very first condition (Age > 5). Once a match is found, Python skips all the other conditions.

    if Age > 60:
        print("Ticket Price 70")

    elif Age > 18:
        print("Ticket price 100")

    elif Age > 5:
        print("Ticket price 50")

    else:
        print("Free entry")


    

if __name__ == "__main__":
    main()