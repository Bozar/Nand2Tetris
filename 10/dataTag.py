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
