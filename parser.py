
from lexer import tokens
from ply.yacc import yacc


def p_expression_equals(p):
    pass

def p_expression_lessthan(p):
    'expression : expression LESSTHAN term'
    p[0] = p[1] < p[3]

def p_expresion_plus(p):
    pass
