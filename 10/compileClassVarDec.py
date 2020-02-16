import handleXML
import verifyXMLline


def compile2xml(text, index):
    labelClass = handleXML.writeLabelPairs('classVarDec')
    startIndex = index
    currentIndex = index
    output = []

    # Add: <classVarDec>.
    output.append(labelClass[0])

    # Move pointer: ('static' | 'field') type varName (',' varName)* ';'.
    while not verifyXMLline.isSemiColon(text[currentIndex]):
        currentIndex += 1
    # Move pointer: classVarDec* | subroutineDec*.
    currentIndex += 1

    # Add: ('static' | 'field') type varName (',' varName)* ';'.
    for i in range(startIndex, currentIndex):
        output.append(text[i])
    # Add: </classVarDec>.
    output.append(labelClass[1])

    return (output, currentIndex)
