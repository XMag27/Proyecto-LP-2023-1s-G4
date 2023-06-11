import ply.lex as lex
#Analizador léxico para Rust

#Diccionario de palabras reservadas
reserved = {
#Xavier Magallanes
  'println': 'PRINT',
  'let': 'LET',
  'mut': 'MUT',
    'fn': 'FN',
    'main': 'MAIN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'loop': 'LOOP',
    'return': 'RETURN',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'true': 'TRUE',
    'false': 'FALSE',
    'struct': 'STRUCT',
    'enum': 'ENUM',
    'impl': 'IMPL',
    'use': 'USE',

}

#Sequencia de tokens, puede ser lista o tupla
tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
          'LLLAVE', 'RLLAVE', 'VARIABLE', 'CADENA', 'PUNTOYCOMA',
          'EXCLAMACION', 'IGUAL', 'COMMA') + tuple(reserved.values())

#Exp Regulares para tokens de símbolos
#Xavier Magallanes
t_PLUS = r'\+'
t_MINUS = r'-'
t_COMMA = r'\,'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_NUMBER = r'\d+'
t_PUNTOYCOMA = r'\;'
t_EXCLAMACION = r'\!'
t_IGUAL = r'\='


#Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


def t_VARIABLE(t):
  r'(_{1}|[a-zA-Z]{1})[a-zA-Z0-9_]*'
  t.type = reserved.get(t.value, 'VARIABLE')
  return t


def t_CADENA(t):
  r'\"{1}.*"{1}'
  t.type = reserved.get(t.value, 'CADENA')
  return t


def t_COMMENT(t):
  r'\/{2}.*'
  pass
  # No return value. Token discarded


# Ignorar lo que no sea un token en mi LP
t_ignore = ' \t'


#Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)


#Contruir analizador
lexer = lex.lex()


data = '''
    let mut x = 5;
    let y = 10;
    let z = x + y;
    println!("El valor de z es: {}", z);
    let mut contador = 0;
    let resultado = loop {
        contador += 1;
        if contador == 10 {
            break contador * 2;
}
};
    println!("El resultado es {}", resultado);
    let a = [10, 20, 30, 40, 50];
    for elemento in a.iter() {
        println!("El valor es: {}", elemento);
}
    for numero in (1..4).rev() {
        println!("{}!", numero);
}
    '''

#Datos de entrada
lexer.input(data)

# Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break  #Rompe
  print(tok)
