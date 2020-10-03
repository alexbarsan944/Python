# 8 Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary
# format is 00011000, meaning 2 bits with value "1"

def count(number: int()):
    def decimalToBinary(num):
        return bin(num).replace("0b", "")

    return str(decimalToBinary(number)).count('1')


print(count(24))
