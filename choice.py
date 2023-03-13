raw = open('skeleton.txt', 'r').read()
want = open('coded.py', 'r').read()

BLOCK_SIZE = 100

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
alphabet += """ (){}[]:'"=,_!|\n\\"""

def get_first_choice(txt):
    try:
        txt[:BLOCK_SIZE].index("[")
    except ValueError:
        return None, None, None

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
    return None, None, None

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
    if len(parsed) == 1:
        parsed.append("")
    return parsed

def choose_block(txt, needle):
    choices, before, after = get_first_choice(txt)

    if choices is None:
        block = txt[:BLOCK_SIZE]
        s = sum(ord(x) for x in block) % len(alphabet)
        if s != needle:
            raise KeyError
        remainder = txt[BLOCK_SIZE:]
        return block, remainder

    for choice in enum_choices(choices):
        try:
            return choose_block(before + choice + after, needle)
        except KeyError:
            pass
    raise KeyError

result = ""
for w in want:
    needle = alphabet.index(w)
    block, remainder = choose_block(raw, needle)
    print(f"---Successfully got '{w}'")
    print("   ..." + block.replace('\n', '\n    ') + "...")
    result += block
    raw = remainder
