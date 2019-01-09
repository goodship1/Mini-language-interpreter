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
    '''if : IF group OPENBRACE print CLOSEBRACE'''
    p[0] =("if-statement",p[4])


def p_else_statement(p):
    '''else : ELSE OPENBRACE print CLOSEBRACE'''
   p[0] = ("else-statement",p[3])


def p_expression_group(p):
    '''expression : OPENINGPARA expression CLOSINGPARA'''
    p[0] = ("group-expression", p[2])


def p_group_lessthan(p):
    '''expression : OPENINGPARA ID LESSTHAN factor CLOSINGPARA'''
    p[0] =("group-lessthan-factor",p[4])


def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = ("number-factor",p[1])

    


def p_expression_add(p):
    '''expression : expression PLUS expression COLON'''
    p[0] = ("add",p[1]+p[3])


def p_expression_minus(p):
    '''expression : expression MINUS expression COLON'''
    p[0] = ("subtract",p[1]-p[3])

def p_expression_times(p):
    '''expression : expression TIMES expression COLON'''
    p[0] = ("mutiplication",p[1]*p[3])
    

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

def add_Operation_test():
    parser = yacc()
    plus_Operation = parser.parse("1+1")
    parser_Result = "('add',(number-factor','1'),(number-factor,'1'))"
    assert(plus_Operation)==parser_Result

def minus_Operation_test():
    parser = yacc()
    minus_Opeartion =  parser.parse('1-1')
    parser_Result  = "('subtraction',(number-factor','1'),(number-factor,'1'))"
    assert(minus_Opeartion) == parser_Result

    
def times_Opeartion_test():
    parser = yacc()
    times_Operation = parse.parser('1*1')
    parser_Result = "('multiplcation',(number-factor','1'),(number-factor,'1'))"
    assert(times_Operation) == parser_Result


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
    
