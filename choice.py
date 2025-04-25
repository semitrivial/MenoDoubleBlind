raw = open('skeleton.txt', 'r').read()
want = open('coded.py', 'r').read()

BLOCK_SIZE = 200

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += " ()[]:'=,+.#\n"
alphabet += '"'

def should_ignore_character(ch):
    if ch == " ":
        return True
    if ch == "\n":
        return True
    if ch == "-":
        return True
    return False

def first_block(txt):
    x = txt[BLOCK_SIZE*4]
    i,cnt=0,0
    while True:
        if not(should_ignore_character(txt[i])):
            cnt += 1
            if cnt == BLOCK_SIZE:
                return txt[:i+1]
        i += 1

def get_first_fork(txt):
    try:
        first_block(txt).index("[")
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
    raise ValueError

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

def myord(x):
    if x == '{':
        return ord("[")
    if x == '}':
        return ord("]")
    return ord(x)

def sum_block(block):
    s = 0
    for ch in block:
        if not(should_ignore_character(ch)):
            s += myord(ch)
    return s

def choose_block(txt, needle):
    choices, before, after = get_first_fork(txt)

    if choices is None:
        block = first_block(txt)
        s = sum_block(block) % len(alphabet)
        if s != needle:
            raise KeyError
        remainder = txt[len(block):]
        return block, remainder

    for choice in enum_choices(choices):
        try:
            return choose_block(before + choice + after, needle)
        except KeyError:
            pass
    raise KeyError

result = ""
for w in want:
    try:
        needle = alphabet.index(w)
    except Exception:
        breakpoint()
    block, remainder = choose_block(raw, needle)
    print(f"---Successfully got '{w}'")
    print("   ..." + block.replace('\n', '\n    ') + "...")
    result += block
    raw = remainder

def findall(needle):
    return [i for i in range(len(result)) if result[i:].startswith(needle)]

dia = open("dialogue.txt", "w")
dia.write(result.replace("{","[").replace("}","]"))
dia.close()
