raw = open('skeleton.txt', 'r').read()
want = open('coded.py', 'r').read()

BLOCK_SIZE = 100

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
alphabet += """(){}[]:'"=,_!|\n\\"""

def get_first_choice(txt):
    depth = 0
    for i in range(len(txt)):
        x = txt[i]
        if x == '[':
            if depth == 0:
                start = i
            depth += 1
        elif x == ']':
            if depth == 0:
                raise ValueError("Unexpected ]")
            elif depth == 1:
                choices = txt[start+1:i]
                before = txt[:start]
                after = txt[i+1:]
                return choices, before, after
            else:
                depth -= 1

def enum_choices(choices):
    depth = 0
    parsed = []
    left = 0
    for i in range(len(choices)):
        x = choices[i]
        if x == '[':
            depth += 1
        elif x == ']':
            depth -= 1
        elif x == '|':
            if depth == 0:
                choice = choices[left:i]
                parsed.append(choice)
                left = i+1
    parsed.append(choices[left:])
    breakpoint()
    return parsed

def choose_block(txt, needle):
    choices, before, after = get_first_choice(txt)

    if choices is None:
        s = sum(ord(x) for x in txt) % len(alphabet)
        if alphabet[s] != needle:
            raise KeyError

    for choice in enum_choices(choices):
        try:
            return choose_block(before + choice + after, needle)
        except KeyError:
            pass

result = ""
for w in want:
    needle = alphabet.index(w)
    result += choose_block(raw, needle)

breakpoint()