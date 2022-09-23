fp = open("plaincode.py", "r")
code = fp.read()
fp.close()
start = code.index('"""')
before = code[:start]
secret = code[start+3:]
end = secret.index('"""')
after = secret[end+3:]
secret = secret[:end]

pwd = "I don't know the password, Socrates."
from random import seed, shuffle, sample
r=range(len(secret))
seed(pwd)
sample(pwd,10)
d = [i for i in r]
shuffle(d)
secret="".join([secret[d.index(i)]for i in r])

coded = before + '"""' + secret + '"""' + after
fp = open("coded.py", "w")
fp.write(coded)
fp.close()

fp = open("skeleton.txt", "r")
dialog = fp.read()
fp.close()
lines = dialog.splitlines()
print(f'Need: {len(coded)/3}, Have: {lines.count("Meno: YES.")}')

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += """(){}[]:'"=,_!|\n\\"""
exec(coded)