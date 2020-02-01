# D = y, M = x.
def popToDandM():
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
def popToD():
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
def pushDtoStack():
    return [
        # Push the result into stack.
        '@SP',
        'A=M',
        'M=D',
        # Increase stack point by 1.
        '@SP',
        'M=M+1',
    ]
