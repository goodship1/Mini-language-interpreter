import ply.lex as lex
import re


"""list of tokens for tokenzing"""

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
t_ignore = "\t"#ignore white spaces



"""more advance rules for token"""


def t_error(t):
    """error handling of lexer"""
    t.lexer.skip(1)



def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.value=reserved[t.value]
    return t


def t_STRING(t):
    r'(\".*\"|\'.*\')'
    t.value = str(t.value[1:-1])
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)
    return t

lex.lex()#builds are lexer with token


toy = """a = 20;
if(a < 10){
    print("wow a is small");
    }
else{
    print(a);
    }
"""

lex.input(toy)

while(True):
    tok = lex.token()
    if not tok:
        break
