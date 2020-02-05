import vmFunctionCall


def writeInit():
    sp = [
        '@256',
        'D=A',
        '@SP',
        'M=D',
    ]
    init = vmFunctionCall.writeCall('Sys.init', '0', 'bootstrap')

    return sp + init
