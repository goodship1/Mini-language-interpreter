import ply.lex


class Lexer(object):
  def __init__(self, program):
    self.program = program
    tokens = ["name","plus","minus","if","else","lessthan"]
