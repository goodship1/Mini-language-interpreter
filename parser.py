
from lexer import tokens
from ply.yacc import yacc

names = dict()#stores names data

precednece = tuple()


def p_assign(p):
    '''assign : ID EQUALS expression COLON'''
    p[0] = p[1]

def p_expression_lessthan(p):
    '''expression: ID LESSTHAN NUMBER'''
    p[0] = p[1] < p[3]

def p_if_statement(p):
    pass

def p_else_statement(p):
    pass

def p_group_expression(p):
    pass

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]


def p_expression_ID(p):
    pass

def p_print_statement(p):
    pass

def p_statement(p):
    pass

yacc()
