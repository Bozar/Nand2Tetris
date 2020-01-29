def translateVMCommand(text):
    stackPoint = '256'
    asmCommand = []
    asmCommand += _setStackPoint(stackPoint)

    for t in text:
        if t[0] == 'C_PUSH':
            asmCommand += _push(t[1], t[2])

    return asmCommand


def _push(arg1, arg2):
    if arg1 == 'constant':
        return [
            '@' + arg2,
            'D=A',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
        ]


def _setStackPoint(stackPoint):
    return [
        '@' + stackPoint,
        'D=A',
        '@SP',
        'M=D',
    ]
