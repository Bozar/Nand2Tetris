import os
import re
import sys

import preProcess
import readWriteFile
import vmBootstrap
import vmCodeWriter
import vmParser


"""
Tips for function calling projects: FibonacciElement, NestedCall, and
StaticsTest.

I spent two days to pass all three tests above and I almost gave up during the
process. Be prepared. They are quite tricky. My first suggestion is to finish
them in the given order. And search the forum when you are in trouble.

http://nand2tetris-questions-and-answers-forum.32033.n3.nabble.com/Project-8-f32620.html

For the FibonacciElement test, make sure you handle the `return` VM command,
especially the `RET = *(FRAME-5)` part correctly. This is where I have made a
mistake. Set breakpoints in your code, perhaps at the end of `return` and `call`
for testing. This might help you to zoom into potential bugs. Refer to the
following link for more information.

http://nand2tetris-questions-and-answers-forum.32033.n3.nabble.com/Function-command-implementation-td4031726.html

For the NestedCall test, I am not sure my mistake is common enough. In
`vmCodeWriter.py`, I insert the function name when processing C_LABEL, C_GOTO
and C_IF commands. I also reset the function name to an empty string when
translating C_RETURN commands. DO NOT reset the string.

For the StaticsTest test, remember that you need to give static data in each vm
file a unique name. The following link contains more hints.

http://nand2tetris-questions-and-answers-forum.32033.n3.nabble.com/One-failed-comparison-with-FibonacciElement-and-StaticsTest-td4031823.html

One more advice. Be careful when using temporary registers: R13, R14 and R15. If
two scripts use these registers in a nested way, that is, `out.py` uses `R13`
and `in.py` uses `R13` and `R14`, this might raise annoying bugs.

Good luck. Happy coding. :)
"""


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
    # Comment this line for projects that do not require a bootstrap.
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
