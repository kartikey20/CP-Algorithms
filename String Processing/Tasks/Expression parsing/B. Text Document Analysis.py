import re
_ = input()
string = input()
in_parenthesis = re.sub(r'\([a-zA-Z_]+\)', '_', string)
out_parenthesis_pattern = re.compile(r'\(([a-zA-Z_]+)\)')
matches = out_parenthesis_pattern.finditer(string)


def calc_max_length(string):
    n = len(string)
    i = 0
    max_len = 0
    length = 0
    while i < n:
        if string[i] in ['_', '(', ')']:
            length = 0
        else:
            length += 1
        max_len = max(max_len, length)
        i += 1
    return max_len


string_length = 0
for match in matches:
    s = list(filter(lambda x: len(x), match.group(1).split('_')))
    string_length += len(s)

print(calc_max_length(in_parenthesis), string_length)
