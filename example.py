import abnex

expr = r'{[w"._-"]1++}"@"{[w"."]1++}'

text = 'lorem ipsum dolor name@example.com lorem ipsum.lorem'
print(abnex.contains(expr, text))
