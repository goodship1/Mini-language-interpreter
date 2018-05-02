
from lexer import tokens
from ply.yacc import yacc


def p_assign(p):
    '''assign : ID EQUALS expression'''
    pass


def p_expression_lessthan(p):
    pass


yacc()
