import pytest
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
        p[0] = ("print-STRING",p[2])
    elif(p[2]== "ID"):
        p[0] =("print-ID",p[2])


def p_error(p):
    print("parser error")




def factor_Assign_test():
    parser = yacc()
    test_Factor = parser.parse("a=20;")
    parser_Result = "('assignment-factor', ('number-factor', '20'))"
    assert(test_Factor)==parser_Result



def error_Test():
    parser = yacc()
    parser_Error = parser.parse("a=1")
    test_Error = "parser error"
    assert(parser_Error) == test_Error




def string_Assign_test():
    parser = yacc()
    test_String_assign = parser.parse("a = 'hello';")
    parser_Result = "('assignment-string',('string','hello'))"
    assert(test_String_assign)==parser_Result



 def lessthan_Statement_test():
     parser = yacc()
     test_Lessthan = parser.parse("a<10")
     parser_Result ="('id-lessthan',('id','a'),('number','10'))"
     assert(parser_Result)==test_Lessthan

def error_test():
    parser = yacc()
    test_Error = parser.parse("aaaaaaa")
    parser_Result = "("parser error")"
    assert(parser_Result)==test_Error
    

def if_Statement_test():
    parser = yacc()
    test_If_statement = parser.parse("""if(a<10){
    print wow a is small;
    }
    else{

        print a;
    }""")
    parser_Result ="('if-statement',('id','a'),('lessthan','number','10'),('print','string'))
    assert(parser_Result)==test_If_statement


def block_test():
    pass



def print_Statement_test_String():
    parser = yacc()
    test_Print_string = parser.parse("print 'hello world';")
    parser_result = "('print-STRING',('STRING','helloworld')"
    assert(parser_Result)==test


def print_Statement_test_Id():
    parser = yacc()
    test_Print_Id = parser.parse("print a;")
    parser_Result ="('print-ID',('ID','a'))"
    assert(parser_Result)==test_Print_Id
    
