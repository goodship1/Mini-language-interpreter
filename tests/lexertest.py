import pytest
import ply.lex as lex
import re

toy_Language = """
        a = 20;
        if(a < 10){
            print("wow a is small");
            }
        else{
            print(a);
            }
        """


string_Test = "hello" #hello should be tokenzed to string and a name and equals as EQUALS
number_Test = "200"
test_Reserved_words = ["if","print","else"]
test_Assignment = "a = hello"
test_Name = "GOODSHIP1"
test_Braces = ['{',"}","(",")"]
test_Operations = ["=","<"]

tests = [string_Test,number_Test,test_Reserved_words,toy_Language,test_Assignment,test_Name]

"""copy of lexer.py source list of tokens for tokenzing"""

reserved = {"if":"IF","else":"ELSE","print":"PRINT"}

tokens = ['NAME',"PLUS","MINUS","EQUALS","LESSTHAN",
            "OPENINGPARA","CLOSINGPARA","OPENBRACE","CLOSINGBRACE",
            "STRING","NUMBER","COLON",""'NEWLINE'
            ]+list(reserved.values())


"""simple tokens"""
t_PLUS = r'\+'
t_PRINT = "print"
t_MINUS= r'-'
t_COLON = r'\;'
t_NUMBER = r'\d+'
t_EQUALS = r'='
t_LESSTHAN = r'\<'
t_OPENINGPARA= r'\('
t_CLOSINGPARA= r'\)'
t_OPENBRACE = r'{'
t_CLOSINGBRACE= r'}'
t_STRING=r'(\".*\"|\'.*\')'
t_ignore = "\t"#ignore white spaces



"""more advance rules for token"""


def t_error(t):
    """error handling of lexer"""
    t.lexer.skip(1)



def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type=reserved[t.value]
    return t





    def t_NEWLINE(t):
        r'\n+'
        t.lexer.lineno+=len(t.value)
        return t

lex.lex()#builds are lexer with token




""" tests for more advance lexer rules"""


def testing_tNUMBER():
    """testing of t_number"""
    lex.input(tests[1])
    tokens = list()
    while True:
        tok = lex.token()
        tokens.append(tok)
        if not tok:
            break      # No more input
    assert("LexToken(NUMBER,'200',1,0)") == str(tokens[0])


def testing_tSTRING():
    """testing of t_number"""
    lex.input(tests[0])
    tokens = list()
    while True:
        tok = lex.token()
        tokens.append(tok)
        if not tok:
            break      # No more input
    assert("LexToken(STRING,'hello',1,0)") == str(tokens[0])




def testing_tNAME():
    """testing of t_NAME"""
    lex.input(test[5])
    tokens = list()
    while True:
        tok = lex.token()
        tokens.append(tok)
        if not tok:
            break
    assert("LexToken(NAME,'GOODSHIP1',1,0)") == str(tokens[5])


def testing_EQUALS():
    pass

def testing_PRINT():
    pass

def testing_LESSTHAN():
    pass

def testing_IF():
    pass

def testing_ELSE():
    pass
