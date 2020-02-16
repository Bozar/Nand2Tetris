import dataTag
import handleXML
from dataTag import tokenType
from dataTag import keyWord


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
