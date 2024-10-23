def main():
    calls = int(input("Enter number of calls: "))
    bill = 200 
    # base bill is 200

    if calls > 200:
        bill += 50 * 0.60 + 50 * 0.50 + (calls - 200) * 0.40
    elif calls > 150:
        bill += 50 * 0.60 + (calls - 150) * 0.50
    elif calls > 100:
        bill += 0.60 * (calls - 100)
    elif calls > 0 and calls <= 100:
        bill += 0

    print(f"Bill is {bill}")

if __name__ == "__main__":
    main()