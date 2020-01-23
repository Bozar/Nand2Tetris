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

    # Read a source file.
    text = []
    text = readWriteFile.readFile(folder, sourceFile)
    # Remove comments, spaces and blank lines.
    text = preProcess.formatText(text)
    # Identify assembly commands.
    parsedCode = []
    parsedCode = hackParse.parse(text)
    # Convert symbols to integers.
    parsedCode = hackSymbolTable.parse(parsedCode)
    # Translate assembly commands to binary codes.
    text = hackCode.translate(parsedCode)
    # Write to a target file.
    readWriteFile.writeFile(folder, targetFile, text)


main()
