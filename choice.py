raw = open('skeleton.txt', 'r').read()
want = open('coded.py', 'r').read()

BLOCK_SIZE = 200

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += " ()[]:'=,+.#\n"
alphabet += '"'

def first_block(txt):
    x = txt[BLOCK_SIZE*4]
    i,cnt=0,0
    while True:
        if (txt[i]!=" ") and (txt[i]!="\n"):
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
        if (ch!=" ") and (ch!="\n"):
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

result = result.replace("defrepeat_twice(X):", "\nSKIP  def repeat_twice(X):")
result = result.replace("print(X)", "\nSKIP    print(X)")
result = result.replace("follows?Goodmorning,Socrates.Goodmorning,Socrates.", "follows?\nSKIP  Good morning, Socrates.\nSKIP  Good morning, Socrates.")
result = result.replace("Wow!Youwin,Socrates!", "\nSKIP  Wow!\nSKIP  You win, Socrates!")
result = result.replace("Meno:Goodmorning,Socrates.Meno:Goodmorning,Socrates.Meno:", "\nSKIP  M_ENO: Good morning, Socrates.\nSKIP  M_ENO: Good morning, Socrates.Meno:")
result = result.replace("Meno:Goodmorning,Socrates.Meno:Goodmorning,Socrates.Socrates:", "\nSKIP  M_ENO: Good morning, Socrates.\nSKIPM_ENO: Good morning, Socrates.Socrates:")
result = result.replace("defoutput_first_ten(X):print(X{:10})", "\nSKIP  def output_first_ten(X):\nSKIP    print(X[:10])")
result = result.replace("defoutput_first_ten_", "\nSKIP  def output_first_ten_")
result = result.replace('X=X.replace("","")#Removespaces', '\nSKIP  X=X.replace(" ","") # Remove spaces')
result = result.replace('X=X.replace("\\n","")#Removeline-breaks', '\nSKIP  X=X.replace("\\n","") # Remove line-breaks')
result = result.replace('X=X.replace("\\t","")#Removetabs', '\nSKIP  X=X.replace("\\t","") # Remove tabs')
result = result.replace("print(X{:10})", "\nSKIP  print(X[:10])")
result = result.replace("Meno:Goodmorning,Socrates.Socrates:GoodAnd", "\nSKIP  Meno:Goodmorning,Socrates.\nSKIP  Socrates:Good\nAnd")
result = result.replace("was:Youwin,Socrates.You'rewelcome.Iadmitit.", "was:\nSKIP  You win, Socrates.\nSKIP  You're welcome.\nSKIP  I admit it.\n")
result = result.replace('print("""Youwin,Socrates.You\'rewelcome.Iadmitit.""")And', '\nSKIP  print("""You win, Socrates.\nSKIP  You\'re welcome.\nSKIP  I admit it.""")\nAnd')
result = result.replace('socrates_line=input("EnterSocrates\'nextline:")ifsocrates_line=="Whatdoyouthink?":print("Ithinkyouwin,Socrates.")else:print("Ithinkyoulose,Socrates."And', '\nSKIP  socrates_line=input("Enter Socrates\' next line: ")\nSKIP  if socrates_line=="What do you think?":\nSKIP    print("I think you win, Socrates.")\nSKIP  else:\nSKIP    print("I think you lose, Socrates."\nAnd')
result = result.replace('alphabet="abcdefghijklmnopqrstuvwxyz"alphabet+="(){}:\'=,+.#\\n"alphabet+=\'"\'', '\nSKIP  alphabet = "abcdefghijklmnopqrstuvwxyz"\nSKIP  alphabet += " (){}:\'=,+.#\\n"\nSKIP  alphabet += \'"\'')
result = result.replace('defcipher(X):total=sum(ord(character)forcharacterinX)remainder=total%len(alphabet)returnalphabet{remainder}This', '\nSKIP  def cipher(X):\nSKIP    total=sum(ord(character) for character in X)\nSKIP    remainder=total%len(alphabet)\nSKIP    return alphabet[remainder]\nThis')
result = result.replace("are:Meno:Goodmorning,Socrates.Socrates:Goodmorningtoyou,Meno,myfriend.Meno:I'vebeenwantingtotalktoyou.Socrates:Andjustwhatwouldyouliketotalkabout,mydearfriend?Meno:It'saboutwhatyousaidthelasttimeyouandIsp", "are:\nSKIP  M_ENO:Goodmorning,Socrates.S_OCRATES:Goodmorningtoyo\nSKIP  u,Meno,myfriend.M_ENO:I'vebeenwantingtotalktoyou.So\nSKIP  crates:Andjustwhatwouldyouliketotalkabout,mydearfr\nSKIP  iend?M_ENO:It'saboutwhatyousaidthelasttimeyouandIsp")
result = result.replace("oketogether.Socrates:IsupposeyoumeanwhenItoldyouthatlearningisreallyjustremembering?Meno:Yes,andthatweactuallyknoweverythingalready,andwemerelyrememberit.Socrates:AndIsupposeyou'vecontrivedsomesortofpWe", "\nSKIP  oketogether.S_OCRATES:IsupposeyoumeanwhenItoldyouth\nSKIP  atlearningisreallyjustremembering?M_ENO:Yes,andthat\nSKIP  weactuallyknoweverythingalready,andwemerelyremembe\nSKIP  rit.S_OCRATES:AndIsupposeyou'vecontrivedsomesortofp\nWe")

result = result.replace("Hewrites'Socrates:'", "Hewrites'S_OCRATES'")
result = result.replace("whetherthis'Socrates:'", "whetherthis'S_OCRATES:'")
result = result.replace("Menosaid'Socrates:'", "Menosaid'S_OCRATES:'")
result = result.replace('output"Meno:Goodmorning,Socrates.Socrates:Goodm"', 'output"M_ENO:Goodmorning,Socrates.S_OCRATES:Goodm"')

result = result.replace("Hewrites'Meno:'", "Hewrites'M_ENO:'")
result = result.replace("Meno:'NowIcan'tremember", "M_ENO:'NowIcan'tremember")
result = result.replace("DidIsay'Meno:'", "DidIsay'M_ENO:'")
result = result.replace("does'Meno:'heremean", "does'M_ENO:'heremean")
result = result.replace("'DidIsayMeno:immediatelyafter...", "'DidIsayM_ENO:immediatelyafter...")
result = result.replace("shallbe'Youwin,Socrates.'Meno:Youwin,Socrates.", "shallbe'Youwin,Socrates.'M_ENO:Youwin,Socrates.")
result = result.replace('"Meno:Youwin,Socrates".', '"M_ENO:Youwin,Socrates".')
result = result.replace('"Youwin,Socrates.Meno:Youwin,Socrates,"Iwould', '"Youwin,Socrates.M_ENO:Youwin,Socrates,"Iwould')
result = result.replace('say,"Meno:Goodmorning,Socrates"?', 'say,"M_ENO:Goodmorning,Socrates"?')
result = result.replace("Itwouldoutput'Meno:'", "Itwouldoutput'M_ENO:'")
result = result.replace("wouldoutput'Meno:Goodm'.", "wouldoutput'M_ENO:Goodm'.")
result = result.replace("'Meno:'and'Good'", "'M_ENO:'and'Good'")
result = result.replace("notoutput'Meno:Goodm'", "notoutput'M_ENO:Goodm'")
result = result.replace("output'Meno:Good',wouldn'tit?", "output'M_ENO:Good',wouldn'tit?")
result = result.replace('with"Meno:Goodmorning,Socrates."', 'with"M_ENO:Goodmorning,Socrates."')
result = result.replace('changes"Meno:"into"p"', 'changes"M_ENO:"into"p"')
result = result.replace('"Meno:Goodm"into"p"', '"M_ENO:Goodm"into"p"')
result = result.replace('cipher("Meno:")', 'cipher("M_ENO:")')

result = result.replace("Socrates:", "\nSocrates:")
result = result.replace("Meno:", "\nMeno:")
result = result.replace("S_OCRATES", "Socrates")
result = result.replace("M_ENO", "Meno")

dia = open("dialogue.txt", "w")
dia.write(result)
dia.close()

breakpoint()