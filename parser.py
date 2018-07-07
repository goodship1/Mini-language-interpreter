
from lexer import tokens
from ply.yacc import yacc


variables = dict()

def p_assign_factor(p):
    '''assign : ID EQUALS factor'''
    p[0] = ('assignment-factor',p[1],p[2],p[3])
    variables[p[1]] = p[3]

def p_assign_string(p):
    '''assign : ID EQUALS STRING COLON'''
    p[0] = ("assign-string",p[3])

def p_expression(p):
    'expression : NUMBER LESSTHAN NUMBER'
    p[0] = ('less-than',p[1]<p[3])


def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = ("number-factor",p[1])



def p_expression_ID(p):
    ''' expression : ID'''
    p[0] = ("id-expression",p[1])

def p_expression_string(p):
    'expression : STRING'
    p[0]  = ("string-expression",p[1])

def p_print(p):
    'print : PRINT ID COLON'
    p[0] = ("print-ID",p[2])


def p_error(p):
    print("parser error")



par = yacc()
result = par.parse("1<20")
print(result)
