import re


def formatText(input):
    output = []
    isBlockComment = False

    for line in input:
        line = _removeLeadingSpace(line)
        line = _removeTrailingSpace(line)
        line = _removeExtraSpace(line)
        line = _removeComment(line)

        if _isEmpty(line):
            continue
        elif _isBlockCommentHead(line):
            isBlockComment = True
            continue
        elif isBlockComment:
            isBlockComment = not _isBlockCommentTail(line)
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
    comment1 = r'\s*//.*$'
    comment2 = r'^/\*.*\*/$'

    input = re.sub(comment1, '', input)
    input = re.sub(comment2, '', input)

    return input


def _isEmpty(input):
    return input == ''


def _isBlockCommentHead(input):
    head = r'^/\*'
    return re.search(head, input) != None


def _isBlockCommentTail(input):
    head = r'\*/$'
    return re.search(head, input) != None
