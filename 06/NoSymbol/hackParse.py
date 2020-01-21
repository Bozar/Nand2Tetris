import re


def _getCommandType(command):
    typeA = 'A_COMMAND'
    typeC = 'C_COMMAND'
    typeL = 'L_COMMAND'

    regA = re.compile(r'^@')
    regL = re.compile(r'^\(.+\)$')

    if regA.search(command) != None:
        return typeA
    elif regL.search(command) != None:
        return typeL
    else:
        return typeC


def _parseACommand(command, parsed):
    regA = re.compile(r'^@(.*)$')
    #                     symbol
    parsed.append(regA.sub(r'\1', command))


def _parseCCommand(command, parsed):
    regFull = re.compile(r'^(.*?)=(.*?);(.*)$')
    #                       dest =comp ;jump
    regNoJump = re.compile(r'^(.*?)=(.*?)$')
    #                         dest =comp
    regNoDest = re.compile(r'^(.*?);(.*?)$')
    #                         comp ;jump

    if regFull.search(command) != None:
        parsed.append(regFull.sub(r'\1', command))
        parsed.append(regFull.sub(r'\2', command))
        parsed.append(regFull.sub(r'\3', command))
    elif regNoJump.search(command) != None:
        parsed.append(regNoJump.sub(r'\1', command))
        parsed.append(regNoJump.sub(r'\2', command))
        parsed.append('')
    else:
        parsed.append('')
        parsed.append(regNoDest.sub(r'\1', command))
        parsed.append(regNoDest.sub(r'\2', command))


def _parseLCommand(command, parsed):
    regL = re.compile(r'^\((.*?)\)$')
    #                     (symbol)
    parsed.append(regL.sub(r'\1', command))


# [commandType, symbol], [commandType, dest, comp, jump]
def parse(command):
    commandType = _getCommandType(command)
    parsedCommand = [commandType]

    if commandType == 'A_COMMAND':
        _parseACommand(command, parsedCommand)
    elif commandType == 'L_COMMAND':
        _parseLCommand(command, parsedCommand)
    elif commandType == 'C_COMMAND':
        _parseCCommand(command, parsedCommand)

    return parsedCommand
