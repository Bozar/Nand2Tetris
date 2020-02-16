import handleXML
import verifyXMLline


def compile2xml(text, index):
    labelClass = handleXML.writeLabelPairs('parameterList')
    startIndex = index
    currentIndex = index
    output = []

    # Add: <parameterList>.
    output.append(labelClass[0])

    # Move pointer: ((type varName) ( ',' type varName)*)? ')'.
    while not verifyXMLline.isRightRoundBracket(text[currentIndex]):
        currentIndex += 1
    # Add: ((type varName) ( ',' type varName)*)? ')'.
    for i in range(startIndex, currentIndex):
        output.append(text[i])

    # Add: </parameterList>.
    output.append(labelClass[1])

    return (output, currentIndex)
