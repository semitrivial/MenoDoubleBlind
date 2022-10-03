import random as a
while 1:
 p=input("passphrase:")
 a.seed (p)
 if "". join(a.sample(p,10))=="a.'nodorss":
  break
x="""print(f'''Meno: ocrat.
Socrates: It didn't predict your 'ocrat'?
Meno: No, or I'd have said the opposite.
Socrates: Maybe the prediction appears if you input the passphrase. And you 
  can study the code first and predict your answer?
Meno: It's encrypted.
Socrates: Then input the passphrase! What is it?
Meno: crate
Socrates: Good, now input the passphrase, which you say is:
    crate
  Maybe then it will predict your 'ocrat'.'''.replace('ocrat','It asks for a passphrase'))"""
d=[i for i in range(len(x))]
a.shuffle(d)
exec("".join(x[i]for i in d).replace('crate',p))