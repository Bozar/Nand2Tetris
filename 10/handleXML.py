import re

import dataTag


def writeLine(label, content):
    label = dataTag.getXMLtag(label)
    content = _convertSymbol(content)
    return '<' + label + '>' + content + '</' + label + '>'


def getContent(line):
    reg = re.compile(r'^<.+>(.*)</.+>$')
    return re.sub(reg, r'\1', line)


def getLabel(line):
    reg = re.compile(r'^<(.+)>.*</.+>$')
    return re.sub(reg, r'\1', line)


def _convertSymbol(symbol):
    symbol2text = {
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        '&': '&amp;',
    }

    if symbol in symbol2text.keys():
        return symbol2text[symbol]
    else:
        return symbol
