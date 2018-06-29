
from lexer import tokens
from ply.yacc import yacc



def p_assign_factor(p):
    '''assign : ID EQUALS factor COLON'''

    p[0] = ('assignment-factor',p[3])

def p_assign_string(p):
    pass

def p_lessthan(p):
    '''expression : ID LESSTHAN factor'''
    p[0] = p[1] < p[3]

def p_ifstatement(p):
    '''if : IF OPENINGPARA ID LESSTHAN factor CLOSINGPARA ELSE'''""
    p[0] = ("lessthan-expression",p[5])


def p_expression_group(p):
    '''expression : OPENBRACE expression CLOSINGBRACE
                  | OPENBRACE factor CLOSINGBRACE'''
    p[0] = ("group", p[2])


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
    p[0] = ("print",p[2])
    print(p[2])


def p_error(p):
    print("parser error")

toy_Language = """
        a = 20;
        if(a < 10){
            print "wow a is small";
            }
        else{
            print a;
            }
        """


ya = yacc()
x = ya.parse("x = hello;")
print(x)
