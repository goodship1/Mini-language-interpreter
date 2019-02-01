
from lexer import tokens
from ply.yacc import yacc


variables = dict()

def p_assign(p):
    '''assign : expression EQUALS expression COLON'''
    p[0] = ('assignment',p[1],p[2],p[3])
    variables[p[1]] = p[3]



def p_expression_id(p):
    '''expression : ID'''
    p[0] = ("id-expression",p[1])

def p_expression_string(p):
    '''expression : STRING'''
    p[0]=("expression-string",p[1])

def p_expression_factor(p):
    'expression : NUMBER'
    p[0]=("number",p[1])


def p_expression_group(p):
    'expression : OPENINGPARA expression CLOSINGPARA'
    p[0]=("group",p[2])


def p_expression_lessthan(p):
    '''expression : expression LESSTHAN expression '''
    p[0] = ("less-than",p[1]<p[3])

def p_expression_minus(p):
    '''expression : expression MINUS expression COLON'''
    p[0] =("subtraction",p[1]-p[3])


def p_expression_times(p):
    '''expression : expression TIMES expression COLON'''
    p[0] = ("mutiplication",p[1]*p[3])


def p_expression_add(p):
    '''expression : expression ADD expression COLON'''
    p[0] = ("add",p[1]+p[3])
    

def p_if(p):
    'if : IF expression OPENINGBRACE print expression CLOSINGBRACE '
    p[0] = ("if-statement",p[5])


def p_else(p):
    'else : ELSE OPENINGBRACE print expression CLOSINGBRACE'
    p[0] =("else-statement",p[3])

def p_print(p):
    'print : PRINT expression COLON'
    p[0] = ("print-statement",p[2])
    print(p[2])

def p_error(p):
    print("parser error")

yacc.yacc()
