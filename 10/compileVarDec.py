import handleXML
import verifyXMLline


def compile2xml(text, index):
    labelClass = handleXML.writeLabelPairs('varDec')
    startIndex = index
    currentIndex = index
    output = []

    # Add: <varDec>.
    output.append(labelClass[0])

    # Move pointer: 'var' type varName (',' varName)* ';'.
    while not verifyXMLline.isSemiColon(text[currentIndex]):
        currentIndex += 1
    # Move pointer.
    currentIndex += 1

    # Add: 'var' type varName (',' varName)* ';'.
    for i in range(startIndex, currentIndex):
        output.append(text[i])
    # Add: </varDec>.
    output.append(labelClass[1])

    return (output, currentIndex)
