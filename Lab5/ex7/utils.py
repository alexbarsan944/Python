# 1) a) Write a module named utils.py that contains one function called process_item. The function will have one
# parameter, x, and will return the least prime number greater than x. When run, the module will request an input
# from the user, convert it to a number and it will display the output of the process_item function.
def process_item(x):
    def isPrime(n):
        if (n <= 1):
            return False
        if (n <= 3):
            return True

        if (n % 2 == 0 or n % 3 == 0):
            return False
        i = 5
        while (i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return False
            i = i + 6
        return True

    x += 1
    while True:
        if isPrime(x):
            return x
        x += 1

# print ("utils loaded")
# print(process_item(int(input("Input number: "))))

