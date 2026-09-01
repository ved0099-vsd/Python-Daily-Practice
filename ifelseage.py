def main():
    print("ENteer your age : ")
    age = int(input())

    if(age <= 18):
        print("You are a minor")
    else:
        print("you are an adult")

if __name__ == "__main__":
    main()