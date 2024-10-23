def main():
    base = int(input("Enter base: "))
    power = int(input("Enter power: "))
    result = 1

    for i in range(1, power+1):
        result = result * base

    print(f"Result is : {result}")

if __name__ == "__main__":
    main()