import ply.lex as lex


class Lexer(object):

  def __init__(self, program):
    self.program = program

  tokens = ("name","plus","minus","lessthan","equals",
            "if","else","leftpara","rightpara","openbrace","closingbrace"
            )

  t_plus = r'\+'
  t_minus = r'-'
  t_lessthan = r'<'
  t_equals = r'='
  t_greaterthan = r'>'
  t_ignore = r'\t'#ignore white spaces
  t_name = r'[a-zA-Z_][a-zA-Z0-9_]*'#names must start with a letter and not a number

  reserved = dict()
