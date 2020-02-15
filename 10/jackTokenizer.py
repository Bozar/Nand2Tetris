import re

import writeXML
from dataTag import tokenType


def tokenize(text):
    splited = []
    output = []
    cachedText = ''
    isInsideString = False

    output += ['<tokens>']
    for line in text:
        splited = list(line)

        for char in splited:
            if isInsideString:
                if _isDoubleQuote(char):
                    isInsideString = False
                    cachedText = writeXML.writeLine(
                        tokenType.STRING_CONST, cachedText)
                    output += [cachedText]
                    cachedText = ''
                else:
                    cachedText += char
            elif _isDoubleQuote(char):
                isInsideString = True
            elif _isSymbol(char) or _isSpace(char):
                cachedText = _tryParseToken(cachedText)
                if cachedText != None:
                    output += [cachedText]
                if _isSymbol(char):
                    cachedText = writeXML.writeLine(tokenType.SYMBOL, char)
                    output += [cachedText]
                cachedText = ''
            else:
                cachedText += char
    output += ['</tokens>']

    return output


def _tryParseToken(text):
    if _isKeyWord(text):
        return writeXML.writeLine(tokenType.KEYWORD, text)
    elif _isInteger(text):
        return writeXML.writeLine(tokenType.INT_CONST, text)
    elif _isIdentifier(text):
        return writeXML.writeLine(tokenType.IDENTIFIER, text)
    else:
        return None


def _isSymbol(char):
    symbols = [
        '{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&',
        '|', '<', '>', '=', '~'
    ]
    return char in symbols


def _isSpace(char):
    return char == ' '


def _isDoubleQuote(char):
    return char == '"'


def _isIdentifier(text):
    identifier = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    return re.search(identifier, text) != None


def _isInteger(text):
    return re.search(r'^\d+$', text) != None


def _isKeyWord(text):
    keyWords = [
        'class', 'constructor', 'function', 'method', 'field', 'static', 'var',
        'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this',
        'let', 'do', 'if', 'else', 'while', 'return'
    ]
    return text in keyWords
