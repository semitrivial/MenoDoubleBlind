yes_grammar = {
  '<YES>': ['<yes>', '<yes>, <Socrates>'],
  '<yes>': ['<affirm>, it <SEEMS>', 'It <SEEMS>'],
  '<affirm>': ['Yes', 'Indeed', 'I admit'],
  '<SEEMS>': ['<seems>', '<adverb> <seems>'],
  '<seems>': ['<does> <seem> <so>', '<seem>s <so>'],
  '<adverb>': ['certainly', 'truly', 'definitely', 'surely'],
  '<seem>': ['seem', 'appear', 'look'],
  '<does>': ['does', 'would'],
  '<so>': ['so', 'to be so', 'it is so', 'that way'],
  '<SOCRATES>': ['<Socrates>', 'my <dear> <Socrates>'],
  '<Socrates>': ['friend', 'companion', 'comrade', 'Socrates'],
  '<dear>': ['<good>', 'most <good>'],
  '<good>': ['dear', 'kind', 'wise', 'faithful', 'noble'],
}

def enum(grammar, txt):
  for key in grammar.keys():
    if key in txt:
      results = []
      for val in grammar[key]:
        results.extend(enum(grammar, txt.replace(key, val)))
      return results
  return [txt]

affirmation_list = enum(yes_grammar, "Meno: <YES>.")

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += """(){}[]:'"=,_!. |\n\\"""

def handle_uppercase(code):
  for letter in alphabet:
    code = code.replace("|"+letter, letter.upper())

print(f'a*a: {len(alphabet)**2}, a*a*a: {len(alphabet)**3}')
print(len(affirmation_list))

def analyze_past(past_dialog):
  code = ""
  for line in past_dialog:
    print(line)
    if line in affirmations:
      code += affirmation_list[affirmations.index(line)]

  code = handle_uppercase(code)
  exec(code)
