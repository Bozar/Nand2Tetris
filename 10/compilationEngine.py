import re

import dataTag
import handleXML
from dataTag import tokenType


def compile(text):
    output = []
    output += _compileClass(text)
    return output


def _isLeftCurlyBracket(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, '{')


def _isRightCurlyBracket(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, '}')


def _isLeftRoundBracket(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, '(')


def _isRightRoundBracket(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, ')')


def _isSemiColon(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, ';')


def _isVarDec(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'var')


def _isLetStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'let')


def _isIfStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'if')


def _isWhileStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'while')


def _isDoStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'do')


def _isReturnStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'return')


def _isClassVarDec(text):
    keyWords = ['static', 'field']
    return text in keyWords


def _isSubroutineDec(text):
    keyWords = ['constructor', 'function', 'method']
    return text in keyWords


def _compileVarDec(text, index):
    indexStart = index
    indexEnd = index
    output = []

    while not _isSemiColon(text[indexEnd]):
        indexEnd += 1
    indexEnd += 1
    for i in range(indexStart, indexEnd):
        output.append(text[i])

    return (output, indexEnd)


def _compileClassVarDec(text, index):
    labelStart = '<classVarDec>'
    labelEnd = '</classVarDec>'
    indexStart = index
    indexEnd = index
    output = [labelStart]

    while not _isSemiColon(text[indexEnd]):
        indexEnd += 1
    indexEnd += 1

    for i in range(indexStart, indexEnd):
        output.append(text[i])
    output.append(labelEnd)

    return (output, indexEnd)


def _compileParameterList(text, index):
    indexStart = index
    indexEnd = index
    output = []

    while not _isRightRoundBracket(text[indexEnd]):
        indexEnd += 1
    for i in range(indexStart, indexEnd):
        output.append(text[i])

    return (output, indexEnd)


def _compileSubroutine(text, index):
    # curlyBracket
    labelStart = '<subroutineDec>'
    labelEnd = '</subroutineDec>'
    output = [labelStart]
    listIndex = ()

    # From start to '('.
    indexStart = index
    indexEnd = index
    while not _isLeftRoundBracket(text[indexEnd]):
        indexEnd += 1
    indexEnd += 1
    for i in range(indexStart, indexEnd):
        output.append(text[i])
    output.append(labelEnd)

    # Parameter list.
    listIndex = _compileParameterList(text, indexEnd)
    output += listIndex[0]
    indexStart = listIndex[1]
    indexEnd = listIndex[1]

    # Add ')' & '{'.
    while not _isLeftCurlyBracket(text[indexEnd]):
        indexEnd += 1
    indexEnd += 1
    for i in range(indexStart, indexEnd):
        output.append(text[i])

    # Add varDec* & statements.
    while not _isRightCurlyBracket(text[indexEnd]):
        if _isVarDec(text[indexEnd]):
            listIndex = _compileVarDec(text, indexEnd)
            output += listIndex[0]
            indexEnd = listIndex[1]
        elif _isLetStatement(text[indexEnd]):
            pass
        elif _isIfStatement(text[indexEnd]):
            pass
        elif _isWhileStatement(text[indexEnd]):
            pass
        elif _isDoStatement(text[indexEnd]):
            pass
        elif _isReturnStatement(text[indexEnd]):
            pass

    output.append(text[indexEnd])
    indexEnd += 1

    return (output, indexEnd)


def _compileClass(text):
    index = 1
    labelStart = '<class>'
    labelEnd = '</class>'
    output = [labelStart]
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
    output += [text[index], labelEnd]

    return output
