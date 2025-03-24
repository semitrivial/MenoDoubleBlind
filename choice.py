raw = open('skeleton.txt', 'r').read()
raw = raw.replace(" ","")
raw = raw.replace("\n", "")
want = open('coded.py', 'r').read()

BLOCK_SIZE = 200

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += " ()[]:'=,+.#\n"
alphabet += '"'

def get_first_fork(txt):
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

def choose_block(txt, needle):
    choices, before, after = get_first_fork(txt)

    if choices is None:
        block = txt[:BLOCK_SIZE]
        s = sum(myord(x) for x in block) % len(alphabet)
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

result = result.replace("defrepeat_twice(X):", "\nSKIP  def repeat_twice(X):")
result = result.replace("print(X)", "\nSKIP    print(X)")
result = result.replace("follows?Goodmorning,Socrates.Goodmorning,Socrates.", "follows?\nSKIP  Good morning, Socrates.\nSKIP  Good morning, Socrates.")
result = result.replace("Wow!Youwin,Socrates!", "\nSKIP  Wow!\nSKIP  You win, Socrates!")
result = result.replace("Meno:Goodmorning,Socrates.Meno:Goodmorning,Socrates.Meno:", "\nSKIP  MENO: Good morning, Socrates.\nSKIP  MENO: Good morning, Socrates.Meno:")
result = result.replace("Meno:Goodmorning,Socrates.Meno:Goodmorning,Socrates.Socrates:", "\nSKIP  MENO: Good morning, Socrates.\nSKIPMENO: Good morning, Socrates.Socrates:")
result = result.replace("defoutput_first_ten(X):print(X{:10})", "\nSKIP  def output_first_ten(X):\nSKIP    print(X[:10])")
result = result.replace("defoutput_first_ten_", "\nSKIP  def output_first_ten_")
result = result.replace('X=X.replace("","")#Removespaces', '\nSKIP  X=X.replace(" ","") # Remove spaces')
result = result.replace('X=X.replace("\\n","")#Removeline-breaks', '\nSKIP  X=X.replace("\\n","") # Remove line-breaks')
result = result.replace('X=X.replace("\\t","")#Removetabs', '\nSKIP  X=X.replace("\\t","") # Remove tabs')
breakpoint()
result = result.replace("print(X{:10})", "\nSKIP  print(X[:10])")
result = result.replace("Meno:Goodmorning,Socrates.Socrates:GoodAnd", "\nSKIP  Meno:Goodmorning,Socrates.\nSKIP  Socrates:Good\nAnd")
result = result.replace("was:Youwin,Socrates.You'rewelcome.Iadmitit.", "was:\nSKIP  You win, Socrates.\nSKIP  You're welcome.\nSKIP  I admit it.\n")
result = result.replace('print("""Youwin,Socrates.You\'rewelcome.Iadmitit.""")And', '\nSKIP  print("""You win, Socrates.\nSKIP  You\'re welcome.\nSKIP  I admit it.""")\nAnd')
result = result.replace('socrates_line=input("EnterSocrates\'nextline:")ifsocrates_line=="Whatdoyouthink?":print("Ithinkyouwin,Socrates.")else:print("Ithinkyoulose,Socrates."And', '\nSKIP  socrates_line=input("Enter Socrates\' next line: ")\nSKIP  if socrates_line=="What do you think?":\nSKIP    print("I think you win, Socrates.")\nSKIP  else:\nSKIP    print("I think you lose, Socrates."\nAnd')
#result = result.replace('alphabet="abcdefghijklmnopqrstuvwxyz"alphabet+=" ()[]:\'=,+.#\\n"alphabet+=\'"\'')
