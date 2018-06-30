
from lexer import tokens
from ply.yacc import yacc



def p_assign_factor(p):
    '''assign : ID EQUALS factor COLON'''

    p[0] = ('assignment-factor',p[3])

def p_assign_string(p):
    '''assign : ID EQUALS STRING COLON'''
    p[0] = ("assign-string",p[3])


def p_lessthan(p):
    '''expression : ID LESSTHAN factor'''
    p[0] = ("lessthan-expression",p[3])

def p_if_statement(p):
    '''if : IF OPENINGPARA ID LESSTHAN factor CLOSINGPARA OPENBRACE PRINT STRING COLON CLOSINGBRACE ELSE OPENBRACE PRINT ID COLON CLOSINGBRACE'''
    p[0] = ("if-else-statement",p[5])


def p_expression_group(p):
    '''expression : OPENINGPARA expression CLOSINGPARA'''
    p[0] = ("group-expression", p[2])


def p_group_lessthan(p):
    '''expression : OPENINGPARA ID LESSTHAN factor CLOSINGPARA'''
    p[0] =("group-lessthan-factor",p[4])


def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = ("number-factor",p[1])



def p_expression_ID(p):
    ''' expression : ID'''
    p[0] = ("id-expression",p[1])

def p_expression_string(p):
    '''expression : STRING'''
    p[0]  = ("string-expression",p[1])

def p_print(p):
    '''expression : PRINT STRING COLON
                 | PRINT ID COLON'''
    if(p[2]== "STRING"):
        p[0] = ("print-string",p[2])
    elif(p[2]== "ID"):
        p[0] =("print-ID",p[2])


def p_error(p):
    print("parser error")

toy_Language = """
        a = 20;
        if(a < 10){
            print "wow a is small";
            }
        """


ya = yacc()
x = ya.parse(toy_Language)
print(x)
