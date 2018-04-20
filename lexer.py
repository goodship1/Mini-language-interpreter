import ply.lex as lex
import re


"""tuple of tokens for tokenzing"""


tokens = ("name","plus","minus","lessthan","equals",
            "if","else","openingpara","closingpara","openbrace","closingbrace",
            "string","number","colon","greaterthan"
            )


"""simple tokens"""
t_plus = r'\+'
t_minus = r'-'
t_colon = r';'
t_lessthan = r'<'
t_equals = r'='
t_greaterthan = r'\>'
t_openingpara = r'\('
t_closingpara = r'\)'
t_openbrace = r'{'
t_closingbrace = r'}'
t_ignore = r't'#ignore white spaces
t_name = r'[a-zA-Z_][a-zA-Z0-9_]*'#names must start with a letter and not a number

reserved = {"print":"PRINT","if":"IF","else":"ELSE"}#reserved key words

"""more advance rules for token"""


def t_number(t):
    """token for ints"""
    r'\d+'
    t.value = int(t.value)
    return t

def t_string(t):
    """token for string"""
    r'(\".*\"|\'.*\')'
    t.value = t.value[1:-1]
    return t


def t_error(t):
    """error handling of lexer"""
    print("this is an error %s"%t.value[0])
    t.skip(1)


lex.lex()
