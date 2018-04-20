import ply.lex as lex
import re


"""list of tokens for tokenzing"""


tokens = ['NAME',"PLUS","MINUS","EQUALS",
            "OPENINGPARA","CLOSINGPARA","OPENBRACE","CLOSINGBRACE",
            "STRING","NUMBER","COLON",'GREATERTHAN','NEWLINE',"IF","ELSE","PRINT"
            ]


"""simple tokens"""
t_PLUS = r'\+'
t_IF = "if"
t_ELSE = "else"
t_PRINT = "print"
t_MINUS= r'-'
t_COLON = r'\;'
t_EQUALS = r'='
t_GREATERTHAN = r'>'
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
    """tokens for name must check if not a reserved word"""
    r'[a-zA-Z_][a-zA-Z0-9_]*'#
    return t

def t_NUMBER(t):
    """token for ints"""
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    """token for string"""
    r'(\".*\"|\'.*\')'
    t.value = t.value[1:-1]
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
    print(tok)
    if not tok:
        break
