import re


def parseVMfile(text):
    parsedCode = []
    line = []
    commandType = ''
    arg1 = ''
    arg2 = ''

    for t in text:
        line = t.split(' ')
        commandType = _getCommandType(line[0])
        arg1 = _getArg1(commandType, line)
        arg2 = _getArg2(commandType, line)

        parsedCode.append([commandType, arg1, arg2])

    return parsedCode


# We return a string instead of an integer. This is different from the
# requirement in the text book.
def _getArg2(commandType, fullCommand):
    validType = ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']

    if commandType in validType:
        return fullCommand[2]
    else:
        return None


def _getArg1(commandType, fullCommand):
    if commandType == 'C_ARITHMETIC':
        return fullCommand[0]
    elif commandType != 'C_RETURN':
        return fullCommand[1]
    else:
        return None


def _getCommandType(command):
    reg2type = {
        '^push': 'C_PUSH',
        '^pop': 'C_POP',
        '^(add|sub|neg|eq|gt|lt|and|or|not)': 'C_ARITHMETIC',
        '^label': 'C_LABEL',
        '^goto': 'C_GOTO',
        '^if-goto': 'C_IF',
        '^function': 'C_FUNCTION',
        '^call': 'C_CALL',
        '^return': 'C_RETURN',
    }

    for reg in reg2type.keys():
        if re.search(reg, command) != None:
            return reg2type[reg]
    return None
