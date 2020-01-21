import convertNumber


def translate(parsedCode):
    typeA = 'A_COMMAND'
    typeC = 'C_COMMAND'

    if parsedCode[0] == typeA:
        return _getACommand(parsedCode[1])
    elif parsedCode[0] == typeC:
        return _getCCommand(parsedCode[1], parsedCode[2], parsedCode[3])


def _getACommand(address):
    decimal = int(address)
    binary = []

    convertNumber.getBinary(decimal, binary)
    _addMissingBit(binary)
    return _joinList(binary)


def _getCCommand(dest, comp, jump):
    binJump = _getBinJump(jump)
    binDest = _getBinDest(dest)
    binComp = _getBinComp(comp)
    head = '111'

    return head + binComp + binDest + binJump


def _addMissingBit(binary):
    maxBit = 16
    while len(binary) < maxBit:
        binary.insert(0, 0)


def _joinList(inputList):
    for i in range(len(inputList)):
        inputList[i] = str(inputList[i])
    return ''.join(inputList)


def _getBinJump(jump):
    asm2bin = {
        '': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }
    return asm2bin[jump]


def _getBinDest(dest):
    asm2bin = {
        '': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }
    return asm2bin[dest]


def _getBinComp(comp):
    asm2bin = {
        '0': '0101010',
        '1': '0111111',
        '-1': '0111010',
        'D': '0001100',
        'A': '0110000',
        '!D': '0001101',
        '!A': '0110001',
        '-D': '0001111',
        '-A': '0110011',
        'D+1': '0011111',
        'A+1': '0110111',
        'D-1': '0001110',
        'A-1': '0110010',
        'D+A': '0000010',
        'D-A': '0010011',
        'A-D': '0000111',
        'D&A': '0000000',
        'D|A': '0010101',
        '!M': '1110001',
        'D&M': '1000000',
        'D|M': '1010101',
        'D+M': '1000010',
        'D-M': '1010011',
        'M': '1110000',
        '-M': '1110011',
        'M+1': '1110111',
        'M-1': '1110010',
        'M-D': '1000111'
    }
    return asm2bin[comp]
