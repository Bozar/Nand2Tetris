import vmArithmetic
import vmFunctionCall
import vmProgramFlow
import vmPushPop


def translateVMCommand(text, symbol):
    stackPoint = '256'
    index = 0
    functionName = ''
    asmCommand = []
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
            asmCommand += vmProgramFlow.writeLabel(t[1], functionName)
        elif t[0] == 'C_GOTO':
            asmCommand += vmProgramFlow.writeGoto(t[1], functionName)
        elif t[0] == 'C_IF':
            asmCommand += vmProgramFlow.writeIf(t[1], functionName)
        elif t[0] == 'C_FUNCTION':
            asmCommand += vmFunctionCall.writeFunction(t[1], t[2])
            functionName = t[1]
        elif t[0] == 'C_CALL':
            asmCommand += vmFunctionCall.writeCall(t[1], t[2], index)
            index += 1
        elif t[0] == 'C_RETURN':
            asmCommand += vmFunctionCall.writeReturn()
            # ERROR: Do not reset functionName. It will cause a bug when calling
            # functions recursively.
            # functionName = ''

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
