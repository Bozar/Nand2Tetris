import asmPushPop
import vmPushPop


# NOTE: This function does not work properly.
def writeCall(functionName, numArgs):
    returnAddress = 'RETURN_ADDRESS$' + functionName
    pushRegD = asmPushPop.pushDtoStack()
    # push return-address
    part1 = [
        '@' + returnAddress,
        'D=A',
        # pushRegD,
    ]
    # push LCL
    part2 = [
        '@LCL',
        'D=M',
        # pushRegD,
    ]
    # push ARG
    part3 = [
        '@ARG',
        'D=M',
        # pushRegD,
    ]
    # push THIS
    part4 = [
        '@THIS',
        'D=M',
        # pushRegD,
    ]
    # push THAT
    part5 = [
        '@THAT',
        'D=M',
        # pushRegD,
    ]
    part6 = [
        # ARG = SP-n-5
        '@SP',
        'D=M',
        '@' + numArgs,
        'D=D-A',
        '@5',
        'D=D-A',
        '@ARG',
        'M=D',
        # LCL = SP
        '@SP',
        'D=M',
        '@LCL',
        'M=D',
        # goto f
        '@' + functionName,
        '0;JMP',
        # (return-address)
        '(' + returnAddress + ')',
    ]
    return\
        part1 + pushRegD +\
        part2 + pushRegD +\
        part3 + pushRegD +\
        part4 + pushRegD +\
        part5 + pushRegD +\
        part6


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


# http://nand2tetris-questions-and-answers-forum.32033.n3.nabble.com/Function-command-implementation-td4031726.html
def writeFunction(functionName, numLocals):
    label = ['(' + functionName + ')']
    repeat = []

    for i in range(int(numLocals)):
        repeat += vmPushPop.push('constant', '0', '')

    return label + repeat
