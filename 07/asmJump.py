def preJump(index):
    return [
        # Store `x-y` into register D.
        'D=M-D',
        # Jump to `TRUE` if D (x-y) is 0.
        # Add `index`, which is an increasing integer, to the label, so that all
        # the labels are unique.
        '@ARITHMETIC_TRUE_' + str(index),
    ]


def postJump(index):
    return [
        # If D (x-y) is not 0, set D (the result) to 0 (false).
        '@0',
        'D=A',
        # Jump to the end of this code block.
        '@ARITHMETIC_END_' + str(index),
        '0;JMP',
        # Set D (the result) to -1 (true).
        '(ARITHMETIC_TRUE_' + str(index) + ')',
        '@0',
        'D=!A',
        # The end of this code block.
        '(ARITHMETIC_END_' + str(index) + ')',
    ]
