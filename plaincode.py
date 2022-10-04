import random as a
x=p="""print('''It wants a password.
It's encrypted.
''',p)"""
while a.sample(p,10)!="a.'nodorss":
 p=input("password:")
 a.seed(p)
d=list(range(len(x)))
a.shuffle(d)
exec("".join(x[i]for i in d))
