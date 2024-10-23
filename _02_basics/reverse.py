def main():
    number = int(input("Enter a number: "))
    reverse = 0

    # their is an easy way, but we are focusing on logic through python
    while(number != 0):
        last_digit = number % 10
        reverse = reverse*10 + last_digit
        number = number // 10

    print(f"reverse is {reverse}")

if __name__ == "__main__":
    main()