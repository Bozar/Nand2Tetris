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
    regA = re.compile(r'^@\s*(\S.*)$')
    #                        symbol
    parsed.append(regA.sub(r'\1', command))


def _parseCCommand(command, parsed):
    regL = re.compile(r'^(\S*?)\s*={0,1}\s*(\S*?)\s*;{0,1}\s*(\S*?)$')
    #                    dest     =        comp     ;        jump
    parsed.append(regL.sub(r'\1', command))
    parsed.append(regL.sub(r'\2', command))
    parsed.append(regL.sub(r'\3', command))


def _parseLCommand(command, parsed):
    regL = re.compile(r'^\(\s*(\S.*?)\s*\)$')
    #                     (   symbol     )
    parsed.append(regL.sub(r'\1', command))


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
