import compileStatements
import compileVarDec
import handleXML
import verifyXMLline


def compile2xml(text, index):
    labelClass = handleXML.writeLabelPairs('subroutineBody')
    startIndex = index
    currentIndex = index
    listIndex = ()
    output = []

    # Add: <subroutineBody>.
    output.append(labelClass[0])
    # Add: '{'.
    output.append(text[currentIndex])

    # Add & move pointer: varDec* statements '}'.
    currentIndex += 1
    while not verifyXMLline.isRightCurlyBracket(text[currentIndex]):
        # Add & move pointer: varDec*'.
        if verifyXMLline.isVarDec(text[currentIndex]):
            listIndex = compileVarDec.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]
        # Add & move pointer: statements.
        else:
            listIndex = compileStatements.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]

    # Add: '}'.
    output.append(text[currentIndex])
    # Add: </subroutineBody>.
    output.append(labelClass[1])
    # Move pointer.
    currentIndex += 1

    return (output, currentIndex)
