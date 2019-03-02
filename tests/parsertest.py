import pytest
from lexer import tokens
from ply.yacc import yacc


def assignment_Number():
    '''testing assignment of number'''
    parser = yacc()
    assignment_Number = parser.parse('x=10;')
    assert(assignment_Number) == "(assignment,'x','=','10')"  

def assignment_String():
    '''test assignmend of string'''
    parser = yacc()
    assignment_String = parser.parse("x='Test';")
    assert(assignment_String) == "(assignment,'x','=',''Test'')
    
    
 
