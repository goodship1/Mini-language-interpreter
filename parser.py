
from lexer import tokens
from ply.yacc import yacc
import AST

variables = dict()

def p_assign(p):
    '''assign : expression EQUALS expression COLON'''
    p[0] = ('assignment',p[1],p[2],p[3])
    variables[p[1]] = p[3]

