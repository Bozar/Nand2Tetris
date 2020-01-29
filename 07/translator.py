import re
import sys

import preProcess
import readWriteFile
import vmCodeWriter
import vmParser


def main():
    # Folder: tmp/.
    # Argument: source folder name.
    folder = sys.argv[1]
    sourceExtension = 'vm'
    targetFile = 'assembly.hack'

    # Read a source file.
    text = []
    text = readWriteFile.readFilesInFolder(folder, sourceExtension)
    # Remove comments, spaces and blank lines.
    text = preProcess.formatText(text)
    # Parse file.
    text = vmParser.parseVMfile(text)
    # Translate command.
    text = vmCodeWriter.translateVMCommand(text)
    # Write to a target file.
    readWriteFile.writeFile(folder, targetFile, text)


main()
