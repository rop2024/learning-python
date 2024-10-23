def main():
    year = int(input("Enter year: "))

    if year % 4 == 0 and year % 100 != 0:
        print("its a leap year")
    else:
        print("its not a leap year")

if __name__ == "__main__":
    main()