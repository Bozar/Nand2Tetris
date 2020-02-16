import compileDoStatement
import compileIfStatement
import compileLetStatement
import compileReturnStatement
import compileWhileStatement
import handleXML
import verifyXMLline


def compile2xml(text, index):
    labelClass = handleXML.writeLabelPairs('statements')
    startIndex = index
    currentIndex = index
    listIndex = ()
    output = []

    # Add: <statements>.
    output.append(labelClass[0])

    # Add & move pointer: statement*.
    while not verifyXMLline.isRightCurlyBracket(text[currentIndex]):
        # Add & move pointer: letStatement.
        if verifyXMLline.isLetStatement(text[currentIndex]):
            listIndex = compileLetStatement.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]
        # Add & move pointer: ifStatement.
        elif verifyXMLline.isIfStatement(text[currentIndex]):
            listIndex = compileIfStatement.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]
        # Add & move pointer: whileStatement.
        elif verifyXMLline.isWhileStatement(text[currentIndex]):
            listIndex = compileWhileStatement.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]
        # Add & move pointer: doStatement.
        elif verifyXMLline.isDoStatement(text[currentIndex]):
            listIndex = compileDoStatement.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]
        # Add & move pointer: returnStatement.
        elif verifyXMLline.isReturnStatement(text[currentIndex]):
            listIndex = compileReturnStatement.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]
        # Move pointer.
        else:
            currentIndex += 1

    # Add: </statements>.
    output.append(labelClass[1])

    return (output, currentIndex)
