import ply.lex as lex
import re

class Lexer(object):

  def __init__(self, program):
    self.program = program

  tokens = ("name","plus","minus","lessthan","equals",
            "if","else","openingpara","closingpara","openbrace","closingbrace",
            "string","number"
            )

  t_plus = r'\+'
  t_minus = r'-'
  t_colon = r';'
  t_lessthan = r'<'
  t_equals = r'='
  t_greaterthan = r'>'
  t_leftpara = r'('
  t_rightpara = r')'
  t_openbrace = r'{'
  t_closingbrace = r'}'
  t_ignore = r'\t'#ignore white spaces
  t_name = r'[a-zA-Z_][a-zA-Z0-9_]*'#names must start with a letter and not a number

  reserved = {"print":"PRINT","if":"IF","else","ELSE"}#reserved key words

  def t_name(self,t):
      """tokenzies names"""
     r'[a-zA-Z_][a-zA-Z0-9_]*'
     return t

  def t_closingbrace(self,t):
      r'\}'
      return t

  def t_openbrace(self,t):
      r'{'
      return t

  def t_leftpara(self,t):
      r'('
      return t

  def t_rightpara(self,t):
      r'\)'
      return t

  def t_equals(self,t):
      r'='
      return t

  def t_greaterthan(self,t):
      r'>'
      return t

  def t_plus(self,t):
      r'+'
      return t

  def t_string(self,t):
      pass

  def t_number(self,t):
      pass


  def t_error(self,t):
      pass




  def run_Lexer(self):

      "used to run lexer"""
      pass
