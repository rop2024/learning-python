def main():
    principle = int(input("Enter principle : "))
    rate = float(input("Enter rate: "))
    time = float(input("Enter time: "))

    interest = float((principle+rate+time)/100)

    print(f"Interest : {interest}")

if __name__ == "__main__":
    main()

