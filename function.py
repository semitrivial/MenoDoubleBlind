yes_grammar = {
  '<YES>': ['<yes>', '<yes>, <Socrates>', 'Indeed, <Socrates>'],
  '<yes>': ['Yes', 'I <think> so', 'It <seems> so', 'It <adverb> <seems> so'],
  '<Socrates>': ['Socrates', 'my friend', 'my <dear> friend'],
  '<dear>': ['dear', 'kind', 'wise', 'faithful', 'noble'],
  '<think>': ['suppose', 'think', 'believe'],
  '<seems>': ['seems', 'appears', 'does seem', 'does appear'],
  '<adverb>': ['certainly', 'truly', 'definitely']
}

def enum(grammar, txt):
  return sum([enum(grammar,txt.replace(k,v)) for (k,v0)
    in grammar.items() for v in v0 if k in txt],[]) or [txt]

def affirmation_list():
  return enum(yes_grammar, '<YES>')

