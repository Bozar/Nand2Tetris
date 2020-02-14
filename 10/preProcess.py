import re


def formatText(input):
    output = []

    for line in input:
        line = _removeLeadingSpace(line)
        line = _removeTrailingSpace(line)
        line = _removeExtraSpace(line)
        line = _removeComment(line)
        if _isEmpty(line):
            continue
        else:
            output.append(line)

    return output


def _removeLeadingSpace(input):
    leading = r'^\s+'
    return re.sub(leading, '', input)


def _removeTrailingSpace(input):
    trailing = r'\s+$'
    return re.sub(trailing, '', input)


def _removeExtraSpace(input):
    extra = r'\s+'
    return re.sub(extra, ' ', input)


def _removeComment(input):
    comment = r'\s*//.*$'
    return re.sub(comment, '', input)


def _isEmpty(input):
    return input == ''
