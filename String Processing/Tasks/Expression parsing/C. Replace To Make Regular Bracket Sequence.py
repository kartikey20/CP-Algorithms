string = input()
open_brackets = {'[': 0, '{': 0, '(': 0}
close_brackets = {']': 0, '}': 0, ')': 0}
brackets = {"square": 0, "round": 0, "curly": 0}
n = len(string)

for i in range(len(string)):
    if string[i] in open_brackets:
        open_brackets[string[i]] += 1
    elif string[i] in close_brackets:
        close_brackets[string]
