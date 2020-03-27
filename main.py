def escape(txt):
    escaped = ''

    for char in txt:
        if char in ['.', '$', '*', '+', '?', '(', ')', '[', '{', '\\']:
            escaped += '\\' + char
        else:
            escaped += char

    return escaped


def get_chars():
    return {
        '(': '{',
        ')': '}',
        '{': '(',
        '}': ')',
        'd': '\\d',
        '*': '.',
        'w': '\\w',
        '_': '\\s',
        'b': '\\b',
        '->': '^',
        '<-': '$',
        '!': '^',
        '0++': '*',
        '1++': '+',
        '0+': '?'
    }


def transpile(char, is_not):
    try:
        return get_chars()[char] if not is_not else get_chars()[char].upper()
    except Exception:
        return char


def parse(expr):
    regex = ''
    tmp = ''

    is_exact = False
    is_skip = False
    is_not = False
    is_quantifier = False

    for index, char in enumerate(expr):
        print(char)
        if is_quantifier:
            tmp += char
            if expr[index + 1] != '+':
                regex += transpile(tmp, is_not)
                tmp = ''
                is_quantifier = False
        elif is_skip:
            is_skip = False
        elif is_exact:
            if char == '"':
                is_exact = False
                tmp = escape(tmp)
                regex += tmp
                tmp = ''
            else:
                tmp += char
        elif char != ' ':
            if char == '"':
                is_exact = True
            elif char == '!' and expr[index - 1] != '[':
                is_not = True
            elif char in ['0', '1'] and expr[index + 1] == '+':
                is_quantifier = True
                tmp = char
            else:
                if index < len(expr)-1:
                    next_up = expr[index + 1]
                    if char == '-' and next_up == '>' or char == '<' and next_up == '-':
                        is_skip = True
                        regex += transpile(char + next_up, is_not)
                    else:
                        regex += transpile(char, is_not)
                else:
                    regex += transpile(char, is_not)

    return regex


expression = '0++ w 1++ w 0+ w'
text = 'Call 1.800-555-1212 for info'

data = parse(expression)
print(data)
