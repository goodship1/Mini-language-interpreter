
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
    'expression : ID LESSTHAN expression'
    p[0] = ('less-than', p[1]<p[3])


def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = ("number-factor",p[1])

def p_group(p):
    'group : OPENINGPARA expression CLOSINGPARA'
    p[0] =('group', p[1])

def p_if_statement(p):
    '''if : IF group OPENBRACE PRINT STRING COLON CLOSINGBRACE ELSE
        | IF group OPENBRACE PRINT ID COLON CLOSINGBRACE ELSE'''
    if(p[5]=="STRING"):
        p[0] = ("if-statement-string",p[5])
    elif(p[5]=="ID"):
        p[0]=("if-statment-id",p[5])

def p_expression_ID(p):
    ''' expression : ID'''
    p[0] = ("id-expression",p[1])

def p_expression_string(p):
    'expression : STRING'
    p[0]  = ("string-expression",p[1])

def p_print(p):
    '''print : PRINT ID COLON
           | PRINT STRING COLON'''
    if(p[1]=='ID'):
        p[0] = ("print-ID",p[2])
    else:
        p[0] = ("print-string",p[2])


def p_error(p):
    print("parser error")



par=yacc()
result = par.parse("(100)")
print(result)
