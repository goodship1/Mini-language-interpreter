import pytest
from lexer import tokens
from ply.yacc import yacc

global parser = yacc()

def assignment_Number():
    '''testing assignment of number test'''
    assignment_Number = global parser.parse('x=10;')
    assert(assignment_Number) == "(assignment,'x','=','10')"  

def assignment_String():
    '''assignment x = 'Test'; test'''
    assignment_String = global parser.parse("x='Test';")
    assert(assignment_String) == "(assignment,'x','=',''Test'')
    
    
 def add_Expression():
    '''number + number colon test'''
    addation_Numbers = global parser.parse("1+1;")
    pass

def minus_Expression():
    ''' number - number colon  test'''
     subtract_Number = global parse.parse('10 - 1;')
     pass


def times_Expression():
    '''number * number colon test'''
    multiplication = global parse.parse("10*10;")
    pass
