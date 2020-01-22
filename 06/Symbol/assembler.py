import re
import sys

import hackCode
import hackParse
import hackSymbolTable
import preProcess
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
    text = preProcess.formatText(text)

    parsedCode = []
    for i in range(len(text)):
        parsedCode = hackParse.parse(text[i])
        parsedCode = hackSymbolTable.parse(text[i])
        text[i] = hackCode.translate(parsedCode)

    readWriteFile.writeFile(folder, targetFile, text)


main()
