from lexer import tokens
from ply.yacc import yacc
import AST

variables = dict()

def p_assign(p):
    '''expression : ID EQUALS expression COLON'''
    p[0] = ('assignment',p[1],p[2],p[3])
    variables[p[1]] = p[3]


def p_term(p):
	'''expression : expression + expression COLON
		      |expression - expression COLON
		      |expression
		      '''
	if(p[2] == '+'):
		p[0] = ("plus" , p[1] + p[3])
	if(p[2] == '-'):
		p[0] = ("minus",p[1] - p[3])
	
	
	
		



def p_Factor(p):
	'''expression : NUMBER'''
	p[0] = p[1]


def p_ID(p):
	'''expression : ID'''
	p[0] = p[1]

def p_lessthan(p):
	'''expression : expression LESSTHAN expression COLON'''
	p[0] = ("less-than" p[1] < p[3])
	
