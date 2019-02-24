from lexer import tokens
from ply.yacc import yacc
import AST

symbol_table = dict()

def p_assign(p):
    '''expression : ID EQUALS expression COLON'''
    p[0] = ('assignment',p[1],p[2],p[3])
    symbol_table[p[1]] = p[3]


def p_add(p):
	'''expression : expression PLUS expression COLON'''
	p[0] = ("add-expression",p[1]+p[3])


def p_minus(p):
	'''expression : expression MINUS expression COLON'''
	p[0] =("minus-expression",p[1]-p[3])


def p_Factor(p):
	'''expression : NUMBER'''
	p[0] = p[1]

def p_String(p):
	'''expression : STRING'''
	p[0] = p[1]
	
	
def p_Id(p):
	'''expression : ID'''
	p[0] = p[1]

def p_lessthan(p):
	'''expression : expression LESSTHAN expression COLON'''
	p[0] = ("less-than", p[1] < p[3])


def p_error(p):
	print "parser error"


x = yacc()
print(x.parse("x = 20;"))



