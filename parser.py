
from lexer import tokens
from ply.yacc import yacc


def p_assign(p):
    '''assign : ID EQUALS expression'''
    p[0] = p[1]


def p_expression_lessthan(p):
    pass

def p_assign_number(p):
    '''assign : ID EQUALS factor'''
    p[0] = p[1]


 def p_expression_if(p):
     pass


yacc()
