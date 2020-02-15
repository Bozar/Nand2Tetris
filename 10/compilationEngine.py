import re

import handleXML


def compile(text):
    output = []
    output += _compileClass(text)
    return output


def _isSemiColon(char):
    return char == ';'


def _isClassVarDec(text):
    keyWords = ['static', 'field']
    return text in keyWords


def _isSubroutineDec(text):
    keyWords = ['constructor', 'function', 'method']
    return text in keyWords


def _compileClassVarDec(text, index):
    labelStart = '<classVarDec>'
    labelEnd = '</classVarDec>'
    output = [labelStart]
    content = ''

    while not _isSemiColon(content):
        content = handleXML.getContent(text[index])
        output += [content]
        index += 1
    output += [labelEnd]
    index += 1

    return (output, index)


def _compileSubroutine(text, index):
    return (text, index)


def _compileClass(text):
    index = 1
    output = ['<class>']
    content = ''
    textIndex = ()

    for i in range(index, index + 3):
        output += [text[i]]
    index += 3

    while index < len(text) - 2:
        content = handleXML.getContent(text[index + 1])
        if _isClassVarDec(content):
            textIndex = _compileClassVarDec(text, index)
            output += textIndex[0]
            index = textIndex[1]
        elif _isSubroutineDec(content):
            textIndex = _compileSubroutine(text, index)
            output += textIndex[0]
            index = textIndex[1]

    output += [text[index]]
    output += ['</class>']

    return output
