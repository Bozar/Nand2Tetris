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

    # Read a source file. Remove comments, spaces and blank lines.
    text = readWriteFile.readFile(folder, sourceFile)
    text = preProcess.formatText(text)

    # Identify assembly commands.
    parsedCode = []
    for command in text:
        parsedCode.append(hackParse.parse(command))

    # Convert symbols to integers.
    hackSymbolTable.parse(parsedCode)

    # Translate assembly commands to binary codes.
    for i in range(len(text)):
        text[i] = hackCode.translate(parsedCode[i])

    # Write to a target file.
    readWriteFile.writeFile(folder, targetFile, text)


main()
