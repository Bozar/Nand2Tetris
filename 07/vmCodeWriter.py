def translateVMCommand(text):
    stackPoint = '256'
    asmCommand = []
    asmCommand += _setStackPoint(stackPoint)

    for t in text:
        if t[0] == 'C_PUSH':
            asmCommand += _push(t[1], t[2])
        elif t[0] == 'C_ARITHMETIC':
            if t[1] == 'add':
                asmCommand += _add()

    return asmCommand


def _add():
    return [
        # Decrease stack point by 1.
        '@SP',
        'M=M-1',
        # Store the popped data into register D.
        '@SP',
        'A=M',
        'D=M',
        # Decrease stack point by 1.
        '@SP',
        'M=M-1',
        # Store the popped data into register M.
        '@SP',
        'A=M',
        # Add data in register D and M.
        'D=D+M',
        # Push the result into stack.
        '@SP',
        'A=M',
        'M=D',
        # Increase stack point by 1.
        '@SP',
        'M=M+1',
    ]


def _push(arg1, arg2):
    if arg1 == 'constant':
        return [
            # Store data into register D.
            '@' + arg2,
            'D=A',
            # Copy data from register D to stack.
            '@SP',
            'A=M',
            'M=D',
            # Increase stack point by 1.
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
