
from lexer import tokens
from ply.yacc import yacc


def p_assign(p):
    '''assign : ID EQUALS expression COLON'''
    pass

def p_expression(p):
    pass

def p_statement(p):
    pass

yacc()
