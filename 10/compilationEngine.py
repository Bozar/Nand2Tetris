import re

import dataTag
import handleXML
from dataTag import tokenType


def compile(text):
    output = []
    output += _compileClass(text)
    return output


def _isSemiColon(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, ';')


def _isClassVarDec(text):
    keyWords = ['static', 'field']
    return text in keyWords


def _isSubroutineDec(text):
    keyWords = ['constructor', 'function', 'method']
    return text in keyWords


def _compileClassVarDec(text, index):
    labelStart = '<classVarDec>'
    labelEnd = '</classVarDec>'
    indexStart = index
    indexEnd = index
    output = [labelStart]

    while not _isSemiColon(text[index]):
        indexEnd += 1
    indexEnd += 1

    for i in range(indexStart, indexEnd):
        output.append(text[index])
    output.append(labelEnd)

    return (output, index)


def _compileSubroutine(text, index):
    return (text, index)


def _compileClass(text):
    index = 1
    output = ['<class>']
    content = ''
    listIndex = ()

    for i in range(index, index + 3):
        output.append(text[i])
    index += 3

    while index < len(text) - 2:
        content = handleXML.getContent(text[index])
        if _isClassVarDec(content):
            listIndex = _compileClassVarDec(text, index)
            output += listIndex[0]
            index = listIndex[1]
        elif _isSubroutineDec(content):
            listIndex = _compileSubroutine(text, index)
            output += listIndex[0]
            index = listIndex[1]
    output += [text[index], '</class>']

    return output
