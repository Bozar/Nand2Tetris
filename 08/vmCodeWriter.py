import vmArithmetic
import vmProgramFlow
import vmPushPop


def translateVMCommand(text, symbol):
    stackPoint = '256'
    index = 0
    asmCommand = []
    asmCommand += _setStackPoint(stackPoint)
    tmpOutput = ()

    for t in text:
        if t[0] == 'C_PUSH':
            asmCommand += vmPushPop.push(t[1], t[2], symbol)
        elif t[0] == 'C_POP':
            asmCommand += vmPushPop.pop(t[1], t[2], symbol)
        elif t[0] == 'C_ARITHMETIC':
            tmpOutput = _getArithmeticCode(t[1], index)
            asmCommand += tmpOutput[0]
            index = tmpOutput[1]
        elif t[0] == 'C_LABEL':
            asmCommand += vmProgramFlow.writeLabel(t[1])
        elif t[0] == 'C_GOTO':
            asmCommand += vmProgramFlow.writeGoto(t[1])
        elif t[0] == 'C_IF':
            asmCommand += vmProgramFlow.writeIf(t[1])

    asmCommand += _setEndlessLoop()

    return asmCommand


def _getArithmeticCode(command, index):
    command2function = {
        'add': vmArithmetic.add,
        'sub': vmArithmetic.sub,
        'neg': vmArithmetic.neg,
        'eq': vmArithmetic.eq,
        'gt': vmArithmetic.gt,
        'lt': vmArithmetic.lt,
        'and': vmArithmetic.logicAnd,
        'or': vmArithmetic.logicOr,
        'not': vmArithmetic.logicNot,
    }
    requireJump = ['eq', 'gt', 'lt']

    if command in requireJump:
        return (command2function[command](index), index + 1)
    else:
        return (command2function[command](), index)


def _setEndlessLoop():
    return [
        '(END_LOOP)',
        '@END_LOOP',
        '0;JMP'
    ]


def _setStackPoint(stackPoint):
    return [
        '@' + stackPoint,
        'D=A',
        '@SP',
        'M=D',
    ]
