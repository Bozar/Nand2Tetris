import asmJump
import asmPushPop


def logicNot():
    pre = asmPushPop.popToD()
    post = asmPushPop.pushDtoStack()
    middle = ['D=!D']
    return pre + middle + post


def logicOr():
    pre = asmPushPop.popToDandM()
    post = asmPushPop.pushDtoStack()
    middle = ['D=D|M']
    return pre + middle + post


def logicAnd():
    pre = asmPushPop.popToDandM()
    post = asmPushPop.pushDtoStack()
    middle = ['D=D&M']
    return pre + middle + post


def lt(index):
    pre = asmPushPop.popToDandM()
    post = asmPushPop.pushDtoStack()
    preJump = asmJump.preJump(index)
    postJump = asmJump.postJump(index)
    middle = ['D;JLT']
    return pre + preJump + middle + postJump + post


def gt(index):
    pre = asmPushPop.popToDandM()
    post = asmPushPop.pushDtoStack()
    preJump = asmJump.preJump(index)
    postJump = asmJump.postJump(index)
    middle = ['D;JGT']
    return pre + preJump + middle + postJump + post


# http://nand2tetris-questions-and-answers-forum.32033.n3.nabble.com/translating-eq-to-asm-td4028370.html
def eq(index):
    pre = asmPushPop.popToDandM()
    post = asmPushPop.pushDtoStack()
    preJump = asmJump.preJump(index)
    postJump = asmJump.postJump(index)
    middle = ['D;JEQ']
    return pre + preJump + middle + postJump + post


def neg():
    pre = asmPushPop.popToD()
    post = asmPushPop.pushDtoStack()
    middle = ['D=-D']
    return pre + middle + post


def sub():
    pre = asmPushPop.popToDandM()
    post = asmPushPop.pushDtoStack()
    middle = ['D=M-D']
    return pre + middle + post


def add():
    pre = asmPushPop.popToDandM()
    post = asmPushPop.pushDtoStack()
    middle = ['D=D+M']
    return pre + middle + post
