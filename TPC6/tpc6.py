import ply.lex as lex

reserved = {
    'int': 'INT',
    'function': 'FUNCTION',
    'program': 'PROGRAM',
    'for': 'FOR',
    'in': 'IN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
}

tokens = [
    'ID', 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LT', 'GT', 'EQ',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 'COMMA', 'SEMI',
    'COMMENT',
] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_EQ = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMI = r';'

t_ignore = ' \t'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_COMMENT(t):
    r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'
    pass

def t_COMMENTLINE(t):
    r'//.*\n'
    pass


def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

with open('factorial.p') as f:
    lexer.input(f.read())
    for tok in lexer:
        print(tok)
