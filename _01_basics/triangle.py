def main():
    i = 0
    sum = 0
    for i in range(3):
        sum += int(input("Enter angle of triangle: "))
    
    if (sum == 180):
        print("It is a triangle")
    
    else:
        print("Not a triangle")


if __name__ == "__main__":
    main()