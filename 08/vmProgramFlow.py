import asmPushPop


def writeLabel(label, functionName):
    return [
        '(' + functionName + '$' + label + ')',
    ]


def writeGoto(label, functionName):
    return [
        '@' + functionName + '$' + label,
        '0;JMP',
    ]


def writeIf(label, functionName):
    pre = asmPushPop.popToD()
    middle = [
        '@' + functionName + '$' + label,
        'D;JNE',
    ]

    return pre + middle
