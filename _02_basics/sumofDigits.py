def main():
    number = int(input("Enter number : "))
    sum = 0

    while( number != 0):
        last_digit = number % 10 
        sum += last_digit
        number = number // 10   
    
    print(f"sum : {sum}")

if __name__ == "__main__":
    main()