import os
import re
import sys

import preProcess
import readWriteFile
import vmBootstrap
import vmCodeWriter
import vmParser


def main():
    # Folder: tmp/.
    # Argument: source folder name.
    folder = sys.argv[1]
    sourceExtension = 'vm'
    targetExtension = 'asm'
    # https://stackoverflow.com/questions/3925096/how-to-get-only-the-last-part-of-a-path-in-python
    partialName = os.path.basename(os.path.normpath(folder))
    targetFile = partialName + '.' + targetExtension

    fileList = readWriteFile.getFileNames(folder, sourceExtension)
    text = []
    asmCode = []
    asmCode += vmBootstrap.writeInit()

    # http://nand2tetris-questions-and-answers-forum.32033.n3.nabble.com/One-failed-comparison-with-FibonacciElement-and-StaticsTest-td4031823.html
    for f in fileList:
        # Read a source file.
        text = readWriteFile.readFile(folder, f)
        # Remove comments, spaces and blank lines.
        text = preProcess.formatText(text)
        # Parse file.
        text = vmParser.parseVMfile(text)
        # Translate command.
        text = vmCodeWriter.translateVMCommand(text, f)
        asmCode += text

    # Write to a target file.
    readWriteFile.writeFile(folder, targetFile, asmCode)


main()
