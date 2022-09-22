from random import seed,random,shuffle
while True:
 p=input("password:")
 seed(p)
 x="".join([alphabet[int(c)]for c in str(random()).replace(".","")])
 if x=="aiadcjfgfffjbcbbc":
  break
x="""s,r,p='|it asks for a pw.','predict','|honestly, sr, |i do not know the pw.'
x=f'''mn: {s}
sr: |it didn't {r} you'd say: {s}?
mn: |no, or I would've said the opposite.
sr: |maybe once you enter the pw, it will show its {r}ion.
  |why don't you read ahead in the code, analyze and anticipate it?
mn: |the code is encrypted.
sr: |then let us enter the password. |what is the pw?
mn: {p}
sr: |go ahead, then. |enter the pw, which according to you is:
    {p}
  |maybe then it will {r} the rest of our discussion. |but now |i must
  depart, mn. Goodbye.'''
for k,v in[("sr","Socrates"),("mn","Meno"),("pw","password")]:
  x=x.replace(k,v)
print(x)"""
r=range(len(x))
d=[i for i in r]
shuffle(d)
x="".join([x[d.index(i)]for i in r])
exec(x)