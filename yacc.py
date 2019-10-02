# Flor Esthela Barbosa Castillo A01281460
# Diseño de compiladores - Tarea 3.2 LITTLEDUCK 2019
# YACC 
 
import sys
import ply.yacc as yacc
from flex import tokens 

# PROGRAMA
def p_programa(p):
    '''
    programa : PROGRAM ID PUNTOYCOMA vars bloque 
             | PROGRAM ID PUNTOYCOMA bloque
    '''
    p[0] = "PROGRAM COMPILED"

# VARS
def p_vars(p):
    '''
    vars : VARS vars1
    '''
def p_vars1(p):
    '''
    vars1 : ID DOSPUNTOS tipo PUNTOYCOMA
          | ID DOSPUNTOS tipo PUNTOYCOMA vars1
          | ID COMA vars1
    '''

# TIPO
def p_tipo(p):
    '''
    tipo : INT
         | FLOAT
    '''

# ESTATUTO
def p_estatuto(p):
    '''
    estatuto : asignacion
             | condicion
             | escritura
    '''

# BLOQUE
def p_bloque(p):
    '''
    bloque : LCORCHE bloque1 RCORCHE
    '''
def p_bloque1(p):
    '''
    bloque1 : estatuto 
            | estatuto bloque1
            | empty
    '''

# VAR CTE
def p_cte(p):
    '''
    cte : ID
        | CTEI
        | CTEF
    '''

# ASIGNACIÓN
def p_asignacion(p):
    '''
    asignacion : ID IGUAL expresion PUNTOYCOMA
    '''

# ESCRITURA
def p_escritura(p):
    '''
    escritura : PRINT LPAREN escritura1 RPAREN PUNTOYCOMA
    '''
def p_escritura1(p):
    '''
    escritura1 : expresion
               | expresion COMA escritura1
               | CTESTRING
               | CTESTRING COMA escritura1
    '''

# EXPRESIÓN
def p_expresion(p):
    '''
    expresion : exp expresion1
    '''
def p_expresion1(p):
    '''
    expresion1 : IZQ exp
               | DER exp
               | IZQDER exp
               | empty
    '''

# CONDICIÓN
def p_condicion(p):
    '''
    condicion : IF LPAREN expresion RPAREN bloque PUNTOYCOMA
              | IF LPAREN expresion RPAREN bloque ELSE bloque PUNTOYCOMA
    '''

# EXP
def p_exp(p):
    '''
    exp : termino exp1
    '''
def p_exp1(p):
    '''
    exp1 : MAS termino exp1
         | MENOS termino exp1
         | empty
    '''

# TÉRMINO
def p_termino(p):
    '''
    termino : factor termino1
    '''
def p_termino1(p):
    '''
    termino1 : ASTERISCO factor termino1
             | SLASH factor termino1
             | empty
    '''

# FACTOR
def p_factor(p):
    '''
    factor : LPAREN expresion RPAREN
           | MAS cte 
           | MENOS cte
           | cte
    '''

def p_empty(p):
    '''empty :'''

def p_error(p):
    print("ERROR {}".format(p))


yacc.yacc()

if __name__ == '__main__':
    try:
        arch_name = 'prueba-2.txt'
        arch = open(arch_name,'r')
        print("Leyendo archivo: " + arch_name + "...")
        info = arch.read()
        # print(info)
        arch.close()
        if(yacc.parse(info, tracking=True) == 'PROGRAM COMPILED'):
            print("SINTAXIS VÁLIDA")
        else:
            print("ERRORES EN LA SINTAXIS") 
    except EOFError:
        print(EOFError)