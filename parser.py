ls
from lexer import tokens
from ply.yacc import yacc
import AST

variables = dict()

def p_assign(p):
    '''assign : ID EQUALS expression COLON'''
    p[0] = ('assignment',p[1],p[2],p[3])
    variables[p[1]] = p[3]


def p_term(p):
	'''term : ID + factor COLON
			| ID - factor COLON
			| factor - factor COLON
			| expression + expression COLON 
			'''
	pass



def p_factor(p):
	'''factor : NUMBER'''
	p[0] = p[1]


def p_Id(p):
	'''expression : ID'''
	p[0] = p[1]

def p_lessthan(p):
	'''expression : ID LESSTHAN factor COLON'''
	p[0] = ("less-than" p[1] < p[3])
	
