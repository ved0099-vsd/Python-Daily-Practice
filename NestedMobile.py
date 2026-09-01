def main():
    PIN = int(input("Enter your PIN : "))
    FingerPrint = input("Have you scanned the Fingerprint ? : (YES/NO)")

    if PIN == 1234:
        if FingerPrint == "YES":
            print("Yes Mobile Unlocked Successfully...!")
        else:
            print("PIN is ok but Fingerprint not scanned ")
    else:
        print("Incorrect PIN")

if __name__ == "__main__":
    main()