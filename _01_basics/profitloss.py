def main():
    selling_price = int(input("Enter selling price : "))
    cost_price = int(input("Enter cost price: "))
    
    if selling_price > cost_price:
        print(f"gain is {selling_price - cost_price}")
    
    else:
        print(f"loss is {cost_price - selling_price}")

main()