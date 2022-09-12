yes_grammar = {
  '<YES>': ['<yes>', '<yes>, <Socrates>', 'Indeed, <Socrates>'],
  '<yes>': ['Yes', 'It <seems> so', 'It <adverb> <seems> so'],
  '<Socrates>': ['Socrates', 'my <friend>', 'my <dear> <friend>'],
  '<friend>': ['friend', 'companion', 'comrade'],
  '<dear>': ['<good>', 'most <good>'],
  '<good>': ['dear', 'kind', 'wise', 'faithful', 'noble'],
  '<seems>': ['seems', 'appears', '<does> <seem>'],
  '<seem>': ['seem', 'appear', 'seem to be', 'appear to be'],
  '<does>': ['does', 'would'],
  '<adverb>': ['certainly', 'truly', 'definitely', 'surely']
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
