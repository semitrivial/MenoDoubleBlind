dialogue_file = open("dialogue.txt", "r")
X = dialogue_file.read()

X=X.replace(" ","") # Remove spaces
X=X.replace("\n","") # Remove linebreaks
X=X.replace("\t","") # Remove tabs
X=X.replace("-","") # Remove hyphens

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += " ()[]:'=,+.#\n"
alphabet += '"'

def cipher(block):
  total = sum(ord(character) for character in block)
  remainder = total % len(alphabet)
  return alphabet[remainder]

i=0
program = ""
while True:
  block = X[i:i+200]
  character = cipher(block)
  program += character

  i += 200
  if "Zeus" in block:
    break

print(program)