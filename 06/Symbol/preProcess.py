import re


def formatText(input):
    output = []

    for line in input:
        line = _removeSpace(line)
        line = _removeComment(line)
        if _isEmpty(line):
            continue
        else:
            output.append(line)

    return output


def _removeSpace(input):
    headTrailSpace = re.compile(r'\s*')
    output = headTrailSpace.sub('', input)

    return output


def _removeComment(input):
    comment = re.compile(r'//.*$')
    return comment.sub('', input)


def _isEmpty(input):
    return input == ''
