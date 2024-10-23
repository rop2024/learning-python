# finding area of circle using radius input from user
from math import pi, pow

def main():
    # enter radius
    radius = float(input("Enter radius: "))

    # compute area of circle
    area = pi * pow(radius,2)

    # print area
    print(f"area : {format(area, "10.2f")}")


if __name__ == "__main__":
    main()