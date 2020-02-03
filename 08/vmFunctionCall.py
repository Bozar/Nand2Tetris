import vmPushPop


def writeCall(functionName, numArgs):
    return []


# Avoid using public registers: R13, R14 and R15. Other scripts might use them
# as well so that their data could be silently changed, which results in
# hard-to-track bugs.
def writeReturn():
    part1 = [
        # FRAME = LCL
        '@LCL',
        'D=M',
        '@TEMP_SAVE_FRAME',
        'M=D',
        # RET = *(FRAME-5)
        '@5',
        'D=A',
        '@TEMP_SAVE_FRAME',
        'D=M-D',
        '@TEMP_SAVE_RET_ADDRESS',
        'M=D',
    ]
    # *ARG = pop()
    part2 = vmPushPop.pop('argument', '0', '')
    part3 = [
        # SP = ARG+1
        '@ARG',
        'D=M+1',
        '@SP',
        'M=D',
        # THAT = *(FRAME-1)
        '@TEMP_SAVE_FRAME',
        'A=M-1',
        'D=M',
        '@THAT',
        'M=D',
        # THIS = *(FRAME-2)
        '@2',
        'D=A',
        '@TEMP_SAVE_FRAME',
        'A=M-D',
        'D=M',
        '@THIS',
        'M=D',
        # ARG = *(FRAME-3)
        '@3',
        'D=A',
        '@TEMP_SAVE_FRAME',
        'A=M-D',
        'D=M',
        '@ARG',
        'M=D',
        # LCL = *(FRAME-4)
        '@4',
        'D=A',
        '@TEMP_SAVE_FRAME',
        'A=M-D',
        'D=M',
        '@LCL',
        'M=D',
        # goto RET
        '@TEMP_SAVE_RET_ADDRESS',
        'A=M',
        '0;JMP',
    ]
    return part1 + part2 + part3


def writeFunction(functionName, numLocals):
    label = ['(' + functionName + ')']
    repeat = []

    for i in range(int(numLocals)):
        repeat += vmPushPop.push('constant', '0', '')

    return label + repeat
