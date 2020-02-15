import sys

import compilationEngine
import jackTokenizer
import preProcess
import readWriteFile


def main():
    # Argument: source folder name.
    folder = sys.argv[1]
    sourceExtension = 'jack'
    targetExtension = 'xml'
    targetFile = ''
    text = []

    fileList = readWriteFile.getFileNames(folder, sourceExtension)

    for f in fileList:
        # Read a source file.
        text = readWriteFile.readFile(folder, f)
        # Remove comments, spaces and blank lines.
        text = preProcess.formatText(text)
        # Tokenize.
        text = jackTokenizer.tokenize(text)
        # Compile.
        text = compilationEngine.compile(text)
        # Write to a target file.
        targetFile = readWriteFile.replaceExtension(f, targetExtension)
        readWriteFile.writeFile(folder, targetFile, text)


main()
