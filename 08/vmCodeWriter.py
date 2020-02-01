import vmArithmetic
import vmPushPop


def translateVMCommand(text, symbol):
    stackPoint = '256'
    index = 0
    asmCommand = []
    asmCommand += _setStackPoint(stackPoint)

    arithmeticFunction = {
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

    for t in text:
        if t[0] == 'C_PUSH':
            asmCommand += vmPushPop.push(t[1], t[2], symbol)
        elif t[0] == 'C_POP':
            asmCommand += vmPushPop.pop(t[1], t[2], symbol)
        elif t[0] == 'C_ARITHMETIC':
            if t[1] in requireJump:
                asmCommand += arithmeticFunction[t[1]](index)
                index += 1
            else:
                asmCommand += arithmeticFunction[t[1]]()
    asmCommand += _setEndlessLoop()

    return asmCommand


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
