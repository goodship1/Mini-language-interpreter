from lexer import tokens
from ply.yacc import yacc

symbol_table = dict()

def p_Assignment(p):
    '''expression : ID EQUALS expression COLON
				  | ID EQUALS NUMBER COLON
				  | ID EQUALS STRING COLON'''
    p[0] = ('assignment',p[1],p[2],p[3])
    symbol_table[p[1]] = p[3]




def p_Addition(p):
	'''expression : ID PLUS NUMBER COLON
				  | NUMBER PLUS NUMBER COLON'''
	p[0] =  ("add" ,p[1],p[2],p[3])


def p_Subtraction(p):
	'''expression : ID MINUS NUMBER COLON
				  | NUMBER MINUS NUMBER COLON'''
	p[0] = ("minus-expression", p[1] , p[2] ,p[3])


def p_Factor(p):
	'''expression : NUMBER'''
	p[0] = p[1]

def p_String(p):
	'''expression : STRING'''
        p[0] = p[1]


	
def p_Multicaption(p):
    '''expression : ID TIMES NUMBER COLON
                  | NUMBER TIMES NUMBER COLON'''
    p[0] = ("times",p[1] , p[2] ,p[3])

	
def p_Id(p):
	'''expression : ID'''
	#needs to check if key word
	p[0] = p[1]

def p_Lessthan(p):
	'''expression : ID LESSTHAN NUMBER COLON
				  | NUMBER LESSTHAN NUMBER COLON
				  | NUMBER LESSTHAN NUMBER'''
	p[0] = ("less-than", p[1] ,p[2], p[3])

def p_Greaterthan(p):
	'''expression : ID GREATERTHAN NUMBER COLON
		      | NUMBER GREATERTHAN NUMBER COLON'''
	p[0] = ("Greaterthan",p[1] ,p[2] , p[3])
	

def p_Print(p):
	'''expression : PRINT NUMBER COLON
				  | PRINT STRING COLON
				  | PRINT expression COLON'''
	p[0] = ("print-statment", p[2])
	print(p[2])
	
def If_Else_statement(p):
	''' if : IF expression  END expression  ELSE END expression '''
	p[0] = ("if-statmenet-else",p[1],p[4],p[7])
	



	
def p_error(p):
	print "parser error"




