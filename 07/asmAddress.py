# Store address data into register A.
def getAddressType1(segment, index):
    seg2Reg = {
        'local': 'LCL',
        'argument': 'ARG',
        'this': 'THIS',
        'that': 'THAT'
    }

    pre = _saveRegisterD()
    post = _setRegisterAandD()
    middle = [
        # Get address and store it into register D.
        '@' + seg2Reg[segment],
        'D=M',
        '@' + index,
        'D=D+A',
    ]

    return pre + middle + post


def getAddressType2(segment, index):
    seg2Reg = {
        'pointer': '3',
        'temp': '5',
    }

    pre = _saveRegisterD()
    post = _setRegisterAandD()
    middle = [
        # Get address and store it into register D.
        '@' + seg2Reg[segment],
        'D=A',
        '@' + index,
        'D=D+A',
    ]

    return pre + middle + post


def getAddressType3(segment, index, symbol):
    pre = _saveRegisterD()
    post = _setRegisterAandD()
    middle = [
        # Get address and store it into register D.
        '@' + symbol + '.' + index,
        'D=A',
    ]

    return pre + middle + post


def _saveRegisterD():
    return [
        # Copy data from register D to R13.
        '@R13',
        'M=D',
    ]


def _setRegisterAandD():
    return [
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
