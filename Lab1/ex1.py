# 1. Find The greatest common divisor of multiple numbers read from the console.


def one():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    def cmmdc(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    print(cmmdc(a, b))
