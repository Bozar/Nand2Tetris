import re
import sys

import preProcess
import readWriteFile


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

    # Write to a target file.
    readWriteFile.writeFile(folder, targetFile, text)


main()
