
from lexer import tokens
from ply.yacc import yacc

names = dict()#stores names data

precednece = tuple()


def p_statment_assign(p):
    '''assign : ID EQUALS expression COLON
              | ID EQUALS factor COLON'''
    p[0] = p[2]

def p_lessthan(p):
    '''expression : ID LESSTHAN expression
                  | ID LESSTHAN factor'''
    p[0] = p[1] < p[3]

def p_ifstatement(p):
    '''if : IF OPENINGPARA expression CLOSINGPARA ELSE
          | IF OPENINGPARA factor CLOSINGPARA ELSE'''
    p[0] = p[3]


def p_expression_group(p):
    '''expression : OPENBRACE expression CLOSINGBRACE
                  | OPENBRACE factor CLOSINGBRACE'''
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

def p_print(p):
    '''statement : PRINT STRING COLON
                 | PRINT ID COLON'''
    print(p[2])


def p_error(p):
    print("parser error")



yacc()
