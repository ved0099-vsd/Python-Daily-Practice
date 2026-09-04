#Student Grade 🎓

#Take marks from 0–100.

#90–100 → A+
#80–89 → A
#70–79 → B
#60–69 → C
#40–59 → D
#Below 40 → Fail

#Also check if the marks are valid. If marks are below 0 or above 100, print "Invalid marks".

def main():
    Marks = int(input("Enter Marks : "))

    if Marks < 0 or Marks > 100:
        print("Invalid Marks")

    elif Marks < 40:
        print("fail")

    elif Marks < 60:
        print("D")

    elif Marks < 70:
        print("C")

    elif Marks < 80:
        print("B")

    elif Marks < 90:
        print("A")
    else:
        print("A+")




if __name__ == "__main__":
    main()