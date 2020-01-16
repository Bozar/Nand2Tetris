def main():
    bin = []
    convertToBinary(42, bin)
    print(bin)


# https://stackoverflow.com/questions/22746429/c-decimal-to-binary-converting
def convertToBinary(decimal, binary):
    if decimal//2 != 0:
        convertToBinary(decimal//2, binary)
    binary.append(decimal % 2)


main()
