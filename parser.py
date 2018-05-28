
from lexer import tokens
from ply.yacc import yacc

names = dict()#stores names data

precednece = tuple()


def p_statment_assign(p):
    '''assign : ID EQUALS expression COLON'''
    p[0] = p[2]

def p_expression_lessthan(p):
    '''expression : ID LESSTHAN expression'''
    p[0] = p[1] < p[3]

def p_if_statement(p):
    '''if : IF OPENINGPARA expression CLOSINGPARA'''
    p[0] = p[2]



def p_expression_group(p):
    '''expression : OPENBRACE expression CLOSINGBRACE'''
    p[0] = p[2]

def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = p[1]


def p_expression_ID(p):
    ''' expression : ID'''
    p[0] = p[1]

def p_expression_string(p):
    '''expression : STRING'''
    p[0]  = p[1]

def p_statment_print(p):
    '''statement : expression'''
    print(p[1])




def p_error(p):
    print("parser error")

yacc()
