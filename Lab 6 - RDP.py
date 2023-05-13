tokens = []
current_index = 0
import re

def parse(input_string):
    global tokens
    global current_index

    tokens = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', input_string)
    current_index = 0

    result = expr()

    if current_token() is not None:
        raise ValueError("Unexpected token at end of input")

    return result

def current_token():
    global tokens
    global current_index

    if current_index < len(tokens):
        return tokens[current_index]
    else:
        return None

def eat(token):
    global current_index

    if current_token() == token:
        current_index += 1
    else:
        raise ValueError(f"Expected '{token}', but got '{current_token()}'")

def factor():
    token = current_token()

    if token is None:
        raise ValueError("Unexpected end of input")

    if token.isdigit():
        eat(token)
        return int(token)
    elif token == '(':
        eat('(')
        result = expr()
        eat(')')
        return result
    else:
        raise ValueError(f"Unexpected token '{token}'")

def term():
    result = factor()

    while current_token() in ('*', '/'):
        if current_token() == '*':
            eat('*')
            result *= factor()
        elif current_token() == '/':
            eat('/')
            result /= factor()

    return result

def expr():
    result = term()

    while current_token() in ('+', '-'):
        if current_token() == '+':
            eat('+')
            result += term()
        elif current_token() == '-':
            eat('-')
            result -= term()

    return result

result = parse("2+3*2")
print(result) 

