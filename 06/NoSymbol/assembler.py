import sys
import readWriteFile


def main():
    # Folder: tmp/.
    # First argument: source file name.
    # Second argument: target file name.
    folder = 'tmp'
    sourceFile = sys.argv[1]
    targetFile = sys.argv[2]
    text = readWriteFile.readFile(folder, sourceFile)

    output = '\n'
    output = output.join(text)
    readWriteFile.writeFile(folder, targetFile, output)


# https://stackoverflow.com/questions/22746429/c-decimal-to-binary-converting
def convertToBinary(decimal, binary):
    # bin = []
    # convertToBinary(42, bin)
    # print(bin)
    if decimal // 2 != 0:
        convertToBinary(decimal // 2, binary)
    binary.append(decimal % 2)


main()
