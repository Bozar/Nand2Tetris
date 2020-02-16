import dataTag
import handleXML
from dataTag import keyWord, tokenType


def isLeftRoundBracket(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, '(')


def isRightRoundBracket(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, ')')


def isLeftCurlyBracket(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, '{')


def isRightCurlyBracket(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, '}')


def isSemiColon(text):
    return text == handleXML.writeLine(tokenType.SYMBOL, ';')


def isLetStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'let')


def isIfStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'if')


def isWhileStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'while')


def isDoStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'do')


def isReturnStatement(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'return')


def isVarDec(text):
    return text == handleXML.writeLine(tokenType.KEYWORD, 'var')


def isClassVarDec(text):
    _static = handleXML.writeLine(
        tokenType.KEYWORD, dataTag.getXMLtag(keyWord.STATIC))
    _field = handleXML.writeLine(
        tokenType.KEYWORD, dataTag.getXMLtag(keyWord.FIELD))
    return text in [_static, _field]


def isSubroutineDec(text):
    _constructor = handleXML.writeLine(
        tokenType.KEYWORD, dataTag.getXMLtag(keyWord.CONSTRUCTOR))
    _function = handleXML.writeLine(
        tokenType.KEYWORD, dataTag.getXMLtag(keyWord.FUNCTION))
    _method = handleXML.writeLine(
        tokenType.KEYWORD, dataTag.getXMLtag(keyWord.METHOD))
    return text in [_constructor, _function, _method]
