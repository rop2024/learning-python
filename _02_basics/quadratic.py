import math
def main():
    ## take input a, b, c
    a = float(input("Enter value of a :"))
    b = float(input("Enter value of b : "))
    c = float(input("Enter value of c :"))

    ## initialize two solution holders
    root1 = root2 = 0.0

    ## compute devidant which is b ^ 2  - 4 * a * c
    discriminant = (b * b) - (4 * a * c)

    ## based on each type, do follow up computation
    if(discriminant > 0):
        ## now if discriminant if positive , then two real solutions
        root1 = (-b + math.sqrt(discriminant))  / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    elif(discriminant < 0):
        ## if devidant is negative, then zero real solutions
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
    else:
        ## if devidant is 0, then one real solutions
        root1 = root2 = - b / (2 * a)

    ## print both the roots in the end
    print(f"Root 1 is {format(root1, ".2f")}")
    print(f"Root 2 is {format(root2, ".2f")}")


if __name__ == "__main__":
    main()