def main():
    Marks = [98,67,78,89,56]

    for no in Marks:
        print(no)

    Marks[2] = 59   #Changes the element at index 2.

    print("-" * 20)

    for no in Marks:
        print(no)


if __name__ == "__main__":
    main()