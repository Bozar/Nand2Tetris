import compileSubroutineBody
import compileParameterList
import handleXML
import verifyXMLline


def compile2xml(text, index):
    labelClass = handleXML.writeLabelPairs('subroutineDec')
    startIndex = index
    currentIndex = index
    listIndex = ()
    output = []

    # Add: <subroutineDec>.
    output.append(labelClass[0])

    # Move pointer: ('constructor' | 'function' | 'method') ('void' | type)
    #               subroutineName '('.
    while not verifyXMLline.isLeftRoundBracket(text[currentIndex]):
        currentIndex += 1
    # Move pointer: parameterList.
    currentIndex += 1
    # Add: ('constructor' | 'function' | 'method') ('void' | type)
    #      subroutineName '('.
    for i in range(startIndex, currentIndex):
        output.append(text[i])

    # Add & move pointer: parameterList.
    listIndex = compileParameterList.compile2xml(text, currentIndex)
    output += listIndex[0]
    currentIndex = listIndex[1]

    # Add: ')'.
    output += text[currentIndex]
    # Move pointer: subroutineBody.
    currentIndex += 1

    # Add & move pointer: subroutineBody.
    listIndex = compileSubroutineBody.compile2xml(text, currentIndex)
    output += listIndex[0]
    currentIndex = listIndex[1]

    # Add: </subroutineDec>.
    output.append(labelClass[1])

    return (output, currentIndex)
