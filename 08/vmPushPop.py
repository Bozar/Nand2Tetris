import asmAddress
import asmPushPop


# Symbol is used as part of the label for static data.
def push(arg1, arg2, symbol):
    pre = []
    post = asmPushPop.pushDtoStack()
    middle = ['D=M']

    if arg1 == 'constant':
        middle = [
            '@' + arg2,
            'D=A',
        ]
    elif arg1 == 'local' or arg1 == 'argument' \
            or arg1 == 'this' or arg1 == 'that':
        pre = asmAddress.getAddressType1(arg1, arg2)
    elif arg1 == 'pointer' or arg1 == 'temp':
        pre = asmAddress.getAddressType2(arg1, arg2)
    elif arg1 == 'static':
        pre = asmAddress.getAddressType3(arg1, arg2, symbol)

    return pre + middle + post


def pop(arg1, arg2, symbol):
    pre = asmPushPop.popToD()
    post = ['M=D']
    middle = []

    if arg1 == 'local' or arg1 == 'argument' \
            or arg1 == 'this' or arg1 == 'that':
        middle = asmAddress.getAddressType1(arg1, arg2)
    elif arg1 == 'pointer' or arg1 == 'temp':
        middle = asmAddress.getAddressType2(arg1, arg2)
    elif arg1 == 'static':
        middle = asmAddress.getAddressType3(arg1, arg2, symbol)

    return pre + middle + post
