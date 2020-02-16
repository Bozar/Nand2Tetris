import compileClassVarDec
import compileSubroutineDec
import handleXML
import verifyXMLline


def compile(text):
    labelClass = handleXML.writeLabelPairs('class')
    startIndex = 1
    currentIndex = 1
    listIndex = ()
    output = []

    # Add: <class>.
    output.append(labelClass[0])
    # Move pointer: 'class' className '{'.
    while not verifyXMLline.isLeftCurlyBracket(text[currentIndex]):
        currentIndex += 1
    # Move pointer: classVarDec*.
    currentIndex += 1
    # Add: 'class' className '{'.
    for i in range(startIndex, currentIndex):
        output.append(text[i])

    # Add & move pointer: classVarDec* subroutineDec* '}'.
    while not verifyXMLline.isRightCurlyBracket(text[currentIndex]):
        # Add & move pointer: classVarDec*.
        if verifyXMLline.isClassVarDec(text[currentIndex]):
            listIndex = compileClassVarDec.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]
        # Add & move pointer: subroutineDec*.
        elif verifyXMLline.isSubroutineDec(text[currentIndex]):
            listIndex = compileSubroutineDec.compile2xml(text, currentIndex)
            output += listIndex[0]
            currentIndex = listIndex[1]
        # Move pointer.
        else:
            currentIndex += 1

    # Add: '}'.
    output.append(text[i])
    # Add: </class>.
    output.append(labelClass[1])

    return output
