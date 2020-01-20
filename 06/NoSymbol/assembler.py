import re
import sys

import readWriteFile


def main():
    # Folder: tmp/.
    # Argument: source file name.
    folder = 'tmp'
    sourceExtension = 'asm'
    targetExtension = 'hack'

    regExt = re.compile('^(.+?\.)' + sourceExtension + '$')
    sourceFile = sys.argv[1]
    targetFile = regExt.sub(r'\1' + targetExtension, sourceFile)

    text = readWriteFile.readFile(folder, sourceFile)

    readWriteFile.writeFile(folder, targetFile, text)


# https://stackoverflow.com/questions/22746429/c-decimal-to-binary-converting
def _convertToBinary(decimal, binary):
    # bin = []
    # convertToBinary(42, bin)
    # print(bin)
    if decimal // 2 != 0:
        _convertToBinary(decimal // 2, binary)
    binary.append(decimal % 2)


main()
