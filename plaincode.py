import random as a
x,w=list("""print('''It wants a password.
It's encrypted.
''',p)"""),"Password: "
p=input(w)
a.seed(p)
if a.sample(p,len(w))=="a.'nodorss":
 a.shuffle(x)
 exec("".join(x))
