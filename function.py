yes_grammar = {
  '<YES>': ['<yes>', '<yes>, <Socrates>', 'Indeed, <Socrates>'],
  '<yes>': ['Yes', 'It <seems> so', 'It <adverb> <seems> so'],
  '<Socrates>': ['Socrates', 'my friend', 'my <dear> friend'],
  '<dear>': ['dear', 'kind', 'wise', 'faithful', 'noble'],
  '<seems>': ['seems', 'appears', 'does seem', 'does appear'],
  '<adverb>': ['certainly', 'truly', 'definitely', 'surely']
}

def enum(grammar, txt):
  return sum([enum(grammar,txt.replace(k,v)) for (k,v0)
    in grammar.items() for v in v0 if k in txt],[]) or [txt]

affirmation_list = enum(yes_grammar, "Meno: <YES>.")

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += """(){}[]:'"=,_!|\n\\"""

def handle_uppercase(code):
  for letter in alphabet:
    code = code.replace("|"+letter, letter.upper())

print(len(alphabet)*len(alphabet))
print(len(affirmation_list))

def analyze_past(past_dialog):
  code = ""
  for line in past_dialog:
    print(line)
    if line in affirmations:
      code += affirmation_list[affirmations.index(line)]

  code = handle_uppercase(code)
  exec(code)
