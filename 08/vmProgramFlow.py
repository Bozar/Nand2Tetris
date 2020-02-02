import asmPushPop


def writeLabel(label):
    return [
        '(' + label + ')',
    ]


def writeGoto(label):
    return [
        '@' + label,
        '0;JMP',
    ]


def writeIf(label):
    pre = asmPushPop.popToD()
    middle = [
        '@' + label,
        'D;JNE',
    ]

    return pre + middle
