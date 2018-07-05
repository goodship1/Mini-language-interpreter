
from lexer import tokens
from ply.yacc import yacc


variables = dict()
def p_assign_factor(p):
    '''assign : ID EQUALS factor COLON'''

    p[0] = ('assignment-factor',p[1],p[2],p[3])

def p_assign_string(p):
    '''assign : ID EQUALS STRING COLON'''
    p[0] = ("assign-string",p[3])


def p_expression_lessthan(p):
    'expression : ID LESSTHAN expression'
    p[0] = ("lessthan-expression",p[3])

def p_if_statement(p):
    '''if : IF OPENINGPARA ID LESSTHAN factor CLOSINGPARA OPENBRACE PRINT STRING COLON CLOSINGBRACE ELSE OPENBRACE PRINT ID COLON CLOSINGBRACE'''
    p[0] = ("if-else-statement",p[5])


def p_expression_group(p):
    '''expression : OPENINGPARA expression CLOSINGPARA'''
    p[0] = ("group-expression", p[2])


def p_group_lessthan(p):
    '''expression : OPENINGPARA ID LESSTHAN expression CLOSINGPARA'''
    p[0] =("group-lessthan-factor",p[4])


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
result = par.parse("(a<10)")
print(result)
