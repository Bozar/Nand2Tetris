def translateVMCommand(text, symbol):
    stackPoint = '256'
    index = 0
    asmCommand = []
    asmCommand += _setStackPoint(stackPoint)

    arithmeticFunction = {
        'add': _add,
        'sub': _sub,
        'neg': _neg,
        'eq': _eq,
        'gt': _gt,
        'lt': _lt,
        'and': _and,
        'or': _or,
        'not': _not,
    }
    requireJump = ['eq', 'gt', 'lt']

    for t in text:
        if t[0] == 'C_PUSH':
            asmCommand += _push(t[1], t[2], symbol)
        elif t[0] == 'C_POP':
            asmCommand += _pop(t[1], t[2], symbol)
        elif t[0] == 'C_ARITHMETIC':
            if t[1] in requireJump:
                asmCommand += arithmeticFunction[t[1]](index)
                index += 1
            else:
                asmCommand += arithmeticFunction[t[1]]()
    asmCommand += _setEndlessLoop()

    return asmCommand


# D = y, M = x.
def _popToDandM():
    return [
        # Decrease stack point by 1.
        '@SP',
        'M=M-1',
        # Store the popped data (y, LIFO) into register D.
        '@SP',
        'A=M',
        'D=M',
        # Decrease stack point by 1.
        '@SP',
        'M=M-1',
        # Store the popped data (x) into register M.
        '@SP',
        'A=M',
    ]


# D = y.
def _popToD():
    return [
        # Decrease stack point by 1.
        '@SP',
        'M=M-1',
        # Store the popped data into register D.
        '@SP',
        'A=M',
        'D=M',
    ]


# D = result.
def _pushDtoStack():
    return [
        # Push the result into stack.
        '@SP',
        'A=M',
        'M=D',
        # Increase stack point by 1.
        '@SP',
        'M=M+1',
    ]


def _preJump(index):
    return [
        # Store `x-y` into register D.
        'D=M-D',
        # Jump to `TRUE` if D (x-y) is 0.
        # Add `index`, which is an increasing integer, to the label, so that all
        # the labels are unique.
        '@ARITHMETIC_TRUE_' + str(index),
    ]


def _postJump(index):
    return [
        # If D (x-y) is not 0, set D (the result) to 0 (false).
        '@0',
        'D=A',
        # Jump to the end of this code block.
        '@ARITHMETIC_END_' + str(index),
        '0;JMP',
        # Set D (the result) to -1 (true).
        '(ARITHMETIC_TRUE_' + str(index) + ')',
        '@0',
        'D=!A',
        # The end of this code block.
        '(ARITHMETIC_END_' + str(index) + ')',
    ]


def _not():
    pre = _popToD()
    post = _pushDtoStack()
    middle = ['D=!D']
    return pre + middle + post


def _or():
    pre = _popToDandM()
    post = _pushDtoStack()
    middle = ['D=D|M']
    return pre + middle + post


def _and():
    pre = _popToDandM()
    post = _pushDtoStack()
    middle = ['D=D&M']
    return pre + middle + post


def _lt(index):
    pre = _popToDandM()
    post = _pushDtoStack()
    preJump = _preJump(index)
    postJump = _postJump(index)
    middle = ['D;JLT']
    return pre + preJump + middle + postJump + post


def _gt(index):
    pre = _popToDandM()
    post = _pushDtoStack()
    preJump = _preJump(index)
    postJump = _postJump(index)
    middle = ['D;JGT']
    return pre + preJump + middle + postJump + post


# http://nand2tetris-questions-and-answers-forum.32033.n3.nabble.com/translating-eq-to-asm-td4028370.html
def _eq(index):
    pre = _popToDandM()
    post = _pushDtoStack()
    preJump = _preJump(index)
    postJump = _postJump(index)
    middle = ['D;JEQ']
    return pre + preJump + middle + postJump + post


def _neg():
    pre = _popToD()
    post = _pushDtoStack()
    middle = ['D=-D']
    return pre + middle + post


def _sub():
    pre = _popToDandM()
    post = _pushDtoStack()
    middle = ['D=M-D']
    return pre + middle + post


def _add():
    pre = _popToDandM()
    post = _pushDtoStack()
    middle = ['D=D+M']
    return pre + middle + post


def _push(arg1, arg2, symbol):
    pre = []
    post = _pushDtoStack()
    middle = ['D=M']

    if arg1 == 'constant':
        middle = [
            '@' + arg2,
            'D=A',
        ]
    elif arg1 == 'local' or arg1 == 'argument' \
            or arg1 == 'this' or arg1 == 'that':
        pre = _getAddressType1(arg1, arg2)
    elif arg1 == 'pointer' or arg1 == 'temp':
        pre = _getAddressType2(arg1, arg2)
    elif arg1 == 'static':
        pre = _getAddressType3(arg1, arg2, symbol)

    return pre + middle + post


def _pop(arg1, arg2, symbol):
    pre = _popToD()
    post = ['M=D']
    middle = []

    if arg1 == 'local' or arg1 == 'argument' \
            or arg1 == 'this' or arg1 == 'that':
        middle = _getAddressType1(arg1, arg2)
    elif arg1 == 'pointer' or arg1 == 'temp':
        middle = _getAddressType2(arg1, arg2)
    elif arg1 == 'static':
        middle = _getAddressType3(arg1, arg2, symbol)

    return pre + middle + post


# Store address data into register A.
def _getAddressType1(segment, index):
    seg2Reg = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT'
    }
    return [
        # Copy data from register D to R13.
        '@R13',
        'M=D',
        # Get address and store it into register D.
        '@' + seg2Reg[segment],
        'D=M',
        '@' + index,
        'D=D+A',
        # Copy address from register D to R14.
        '@R14',
        'M=D',
        # Copy data from register R13 to D.
        '@R13',
        'D=M',
        # Copy address from register R14 to A.
        '@R14',
        'A=M',
    ]


def _getAddressType2(segment, index):
    seg2Reg = {
        'pointer': '3',
        'temp': '5',
    }
    return [
        # Copy data from register D to R13.
        '@R13',
        'M=D',
        # Get address and store it into register D.
        '@' + seg2Reg[segment],
        'D=A',
        '@' + index,
        'D=D+A',
        # Copy address from register D to R14.
        '@R14',
        'M=D',
        # Copy data from register R13 to D.
        '@R13',
        'D=M',
        # Copy address from register R14 to A.
        '@R14',
        'A=M',
    ]


def _getAddressType3(segment, index, symbol):
    return [
        # Copy data from register D to R13.
        '@R13',
        'M=D',
        # Get address and store it into register D.
        '@' + symbol + '.' + index,
        'D=A',
        # Copy address from register D to R14.
        '@R14',
        'M=D',
        # Copy data from register R13 to D.
        '@R13',
        'D=M',
        # Copy address from register R14 to A.
        '@R14',
        'A=M',
    ]


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
