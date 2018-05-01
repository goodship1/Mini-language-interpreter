
from lexer import tokens
from ply.yacc import yacc


def p_expression_equals(p):
    'term : term EQUALS factor'
    p[0] = p[1]


def p_expression_lessthan(p):
    'expression : term LESSTHAN term'
    p[0] = p[1] < p[3]



def p_expression_print(p):
    pass

parser = yacc()
