import random as a
x=list("""print('''It wants a password.
It's encrypted.
''',p)""")
P=p="Password: "
while a.sample(p,len(P))!="a.'nodorss":
 p=input(P)
 a.seed(p)
a.shuffle(x)
exec("".join(x))