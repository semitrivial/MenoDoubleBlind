import random as a
while 1:
 p=input("passphrase:")
 a.seed (p)
 if "". join(a.sample(p,10))=="a.'nodorss":
  break
x="""print(f'''Meno: It asks for a passphrase.
Meno: No, or I'd have said the opposite.
Meno: It's encrypted.
Meno: '''+p)"""
d=[i for i in range(len(x))]
a.shuffle(d)
exec("".join(x[i]for i in d)
