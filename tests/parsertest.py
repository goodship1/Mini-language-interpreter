import pytest
from lexer import tokens
from ply.yacc import yacc

def p_Number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_assignment(p):
    '''expression : ID EQUALS expression COLON'''
    pass


def assignment_Number():
    '''testing assignment of number'''
    pass

def assignment_String():
    '''test assignmend of string'''
    pass


