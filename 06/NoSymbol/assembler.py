import sys
import readWriteFile


def main():
    # bin = []
    # convertToBinary(42, bin)
    # print(bin)

    # Read tmp/Add.asm. Input `Add.asm` as the first argument.
    folder = 'tmp'
    asmFileName = sys.argv[1]
    text = readWriteFile.readFile(folder, asmFileName)

    print(text)


# https://stackoverflow.com/questions/22746429/c-decimal-to-binary-converting
def convertToBinary(decimal, binary):
    if decimal // 2 != 0:
        convertToBinary(decimal // 2, binary)
    binary.append(decimal % 2)


main()
