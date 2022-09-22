import random as a
while 1:
 p=input("password:")
 a.seed(p)
 x="".join([alphabet[int(c)]for c in str(a.random())[len(".."):]])
 if x=="iadcjfgfffjbcbbc":
  break
x="""s,r='|it asks for a pw.','predict'
x=f'''mn: {s}
sr: |it didn't {r} you'd say: {s}?
mn: |no, or I'd have said the opposite.
sr: |maybe the {r}ion appears if you enter the pw. |why don't
  you study the code first, analyze and anticipate it?
mn: |it's encrypted.
sr: |then let us enter the password. |what is the pw?
mn: {p}
sr: |good. |enter the pw, which according to you is:
    {p}
  |maybe then it will {r} your line, '{s}'.'''
for k,v in[("sr","Socrates"),("mn","Meno"),("pw","password")]:
  x=x.replace(k,v)
print(x)"""
d=[i for i in range(len(x))]
a.shuffle(d)
exec("".join(x[i]for i in d))