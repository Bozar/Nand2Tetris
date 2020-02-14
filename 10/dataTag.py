from enum import Enum, auto


class tokenType(Enum):
    KEYWORD = auto(),
    SYMBOL = auto(),
    IDENTIFIER = auto(),
    INT_CONST = auto(),
    STRING_CONST = auto(),


class keyWord(Enum):
    CLASS = auto(),
    METHOD = auto(),
    FUNCTION = auto(),
    CONSTRUCTOR = auto(),
    INT = auto(),
    BOOLEAN = auto(),
    CHAR = auto(),
    VOID = auto(),
    VAR = auto(),
    STATIC = auto(),
    FIELD = auto(),
    LET = auto(),
    DO = auto(),
    IF = auto(),
    ELSE = auto(),
    WHILE = auto(),
    RETURN = auto(),
    TRUE = auto(),
    FALSE = auto(),
    NULL = auto(),
    THIS = auto(),


def getXMLtag(enumTag):
    enum2string = {
        tokenType.KEYWORD: 'keyword',
        tokenType.SYMBOL: 'symbol',
        tokenType.IDENTIFIER: 'identifier',
        tokenType.INT_CONST: 'integerConstant',
        tokenType.STRING_CONST: 'stringConstant',

        keyWord.CLASS: 'class',
        keyWord.METHOD: 'method',
        keyWord.FUNCTION: 'function',
        keyWord.CONSTRUCTOR: 'constructor',
        keyWord.INT: 'int',
        keyWord.BOOLEAN: 'boolean',
        keyWord.CHAR: 'char',
        keyWord.VOID: 'void',
        keyWord.VAR: 'var',
        keyWord.STATIC: 'static',
        keyWord.FIELD: 'field',
        keyWord.LET: 'let',
        keyWord.DO: 'do',
        keyWord.IF: 'if',
        keyWord.ELSE: 'else',
        keyWord.WHILE: 'while',
        keyWord.RETURN: 'return',
        keyWord.TRUE: 'true',
        keyWord.FALSE: 'false',
        keyWord.NULL: 'null',
        keyWord.THIS: 'this',
    }

    return enum2string[enumTag]
