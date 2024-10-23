def main():
    number = int(input("Enter number : "))

    factorial = 1

    for i in range(1,number+1):
        # 1 is starting position and number + 1 is last(as loop goes till number - 1)
        factorial *= i

    print(f"factrial of {number} is {factorial}")

main()