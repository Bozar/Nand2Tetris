import re


def parse(parsedCode):
    typeA = 'A_COMMAND'
    typeL = 'L_COMMAND'
    symbolTable = _getPredefinedSymbol()

    _addLabelToSymbolTable(parsedCode, symbolTable)
    _parseSymbol(parsedCode, symbolTable)


def _parseSymbol(parsedCode, symbolTable):
    varAddress = 16

    for i in range(len(parsedCode)):
        if _isLCommand(parsedCode[i][0]):
            parsedCode[i][1] = symbolTable[parsedCode[i][1]]
        elif _isACommand(parsedCode[i][0]) and _isSymbol(parsedCode[i][1]):
            if parsedCode[i][1] not in symbolTable.keys():
                symbolTable[parsedCode[i][1]] = str(varAddress)
                varAddress += 1
            parsedCode[i][1] = symbolTable[parsedCode[i][1]]


def _addLabelToSymbolTable(parsedCode, symbolTable):
    lineCount = 0

    for i in range(len(parsedCode)):
        if _isLCommand(parsedCode[i][0]):
            symbolTable[parsedCode[i][1]] = str(lineCount)
            # symbolTable[parsedCode[i][1]] = str(lineCount + 1)
        else:
            lineCount += 1


def _isLCommand(checkType):
    typeL = 'L_COMMAND'
    return checkType == typeL


def _isACommand(checkType):
    typeA = 'A_COMMAND'
    return checkType == typeA


def _isSymbol(checkValue):
    regSymbol = re.compile(r'^\d')
    return regSymbol.search(checkValue) == None


def _getPredefinedSymbol():
    symbols = {
        'SP': '0',
        'LCL': '1',
        'ARG': '2',
        'THIS': '3',
        'THAT': '4',
        'SCREEN': '16384',
        'KBD': '24576',
        'R0': '0',
        'R1': '1',
        'R2': '2',
        'R3': '3',
        'R4': '4',
        'R5': '5',
        'R6': '6',
        'R7': '7',
        'R8': '8',
        'R9': '9',
        'R10': '10',
        'R11': '11',
        'R12': '12',
        'R13': '13',
        'R14': '14',
        'R15': '15'
    }
    return symbols
