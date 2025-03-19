import random as a
while 1:
 p=input("please enter the password: ").lower()
 a.seed(p)
 x="".join(a.sample(p,len(p)))
 if x=="decstedok.w wh , o nasot  aorroptnsis":
  break
x="""s='it asks for a pw'
r='predict'
x=f'''mn: {s}.

sr: it didn't {r} you'd say: {s}?

mn: no, or i'd have said the opposite.

sr: maybe the {r}ion appears if you enter the pw. why don't
  you study the code first, analyze and anticipate it?

mn: it's encrypted.

sr: then let us enter the pw. what is the pw?

mn: {p}

sr: good. enter the pw, which according to you is:
    "{p}"
  maybe then it will {r} your response.'''
x=x.replace("sr","socrates")
x=x.replace("mn","meno")
x=x.replace("pw","password")
print(x)"""
d=[i for i in range(len(x))]
a.shuffle(d)
exec("".join(x[i]for i in d))