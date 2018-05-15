
from lexer import tokens
from ply.yacc import yacc


def p_assign(p):
    '''assign : ID EQUALS expression COLON'''
    p[0] = p[1]

def p_expression(p):
    '''expression: ID LESSTHAN term'''
    p[0] = p[1] < p[2]

def p_if_statement(p):
    pass

def p_else_statement(p):
    pass

def p_expression_number(p):
    pass

def p_expression_ID(p):
    pass

def p_print_statement(p):
    pass

def p_statement(p):
    pass

yacc()
