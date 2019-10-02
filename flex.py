# Flor Esthela Barbosa Castillo A01281460
# Diseño de compiladores - Tarea 3.2 LITTLEDUCK 2019
# FLEX 

import syssdfsdf
import ply.lex as lex

reserved = {
    'program' : 'PROGRAM',
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'vars' : 'VARS',
    'int' : 'INT',
    'float' : 'FLOAT'
}

tokens = [
    'ID',
    'CTEI',
    'CTEF',
    'CTESTRING',
    'LPAREN',
    'RPAREN',
    'DOSPUNTOS',
    'PUNTOYCOMA',
    'PUNTO',
    'COMA',
    'LCORCHE',
    'RCORCHE',
    'IGUAL',
    'ASTERISCO',
    'SLASH',
    'IZQ', 
    'DER', 
    'IZQDER', 
    'MAS',
    'MENOS'
] + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    # t.type = 'ID'
    return t

def t_CTEI(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DOSPUNTOS = r'\:'
t_PUNTO = r'\.'
t_COMA = r'\,'
t_PUNTOYCOMA = r'\;'
t_LCORCHE = r'\{'
t_RCORCHE = r'\}'
t_IGUAL = r'\='
t_ASTERISCO = r'\*'
t_SLASH = r'/'
t_IZQ = r'\>'
t_DER = r'\<'
t_IZQDER = r'\<>'
t_MAS = r'\+'
t_MENOS = r'\-'
t_CTESTRING = r'\".*\"'

t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
 
lexer = lex.lex()