# edvard expressions
Dvard expressions is an alternative to regular expressions.

# Translations
### Regex on right after -> is the edvard expressions equivalent
## Anchors
- Start of string, or start of line in multi-line pattern
  - `^` -> `-sm>`
- End of string, or end of line in multi-line pattern
  - `$` -> `<sm-`
- Start of string
  - `\A` -> `-s>`
- End of string
  - `\Z` -> `<s-`
- Word boundary
  - `\b` -> `:`
- Not word boundary
  - `\B` -> `!:`
- Start of word
  - `\<` -> `-c>`
- End of word
  - `\>` -> `<c-`

## Character Classes
- Control character
  - `\c` -> `c`
- White space
  - `\s` -> `_`
- Not white space
  - `\S` -> `!_`
- Digit
  - `\d` -> `d`
- Not digit
  - `\D` -> `!d`
- Word
  - `\w` -> `c`
- Not word
  - `\W` -> `!c`
- Hexade­cimal digit
  - `\x` -> `x`
- Octal digit
  - `\o` -> `o`

## Quantifiers
- 0 or more
  - `*` -> `0++`
- 1 or more
  - `+` -> `1++`
- 0 or 1
  - `?` -> `0+`

## Groups and Ranges
- Any character except new line (\n)
  - `.` -> `*`
- a or b
  - `a|b` -> `"a"|"b"`
- Group
  - `(...)` -> `{...}`
- Passive (non-c­apt­uring) group
  - `(?:...)` -> `{#...}`
- Range (a or b or c)
  - `[abc]` -> `['abc']` or `["a" "b" "c"]`
- Not in set
  - `[^...]` -> `[!...]`
- Lower case letter from a to q
  - `[a-q]` -> `['a-q']`
- Upper case letter from A to Q
  - `[A-Q]` -> `['A-Q']`
- Digit from 0 to 7
  - `[0-7]` -> `['0-7']`

