import re


def _removeSpace(input):
    headTrailSpace = re.compile(r'\s*')
    output = headTrailSpace.sub('', input)

    return output


def _isComment(input):
    comment = re.compile(r'^//')
    output = comment.search(input)

    return output != None


def _isEmpty(input):
    return input == ''


def formatText(input):
    output = []

    for line in input:
        line = _removeSpace(line)
        if (_isComment(line) or _isEmpty(line)):
            continue
        else:
            output.append(line)

    return output
