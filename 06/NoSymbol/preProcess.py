import re


def _removeHeadTrailSpace(input):
    headTrailSpace = re.compile(r'^\s*(.*?)\s*$')
    output = headTrailSpace.sub(r'\1', input)

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
        line = _removeHeadTrailSpace(line)
        if (_isComment(line) or _isEmpty(line)):
            continue
        else:
            output.append(line)

    return output
