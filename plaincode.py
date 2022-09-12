from random import seed, random, shuffle
a=alphabet
while True:
  p=input("password:")
  seed(p)
  x="".join([a[int(c)]for c in str(random())[2:]])
  if x=="iadcjfgfffjbcbbc":
    break

x="""s='It prints the dialog so far, then asks for a pw.'
x=f'''mn: {s}
sr: That's clever, mn.
mn: How so?
sr: Suppose it had predicted you'd say:
    "{s}"
  What would you have said then?
mn: The opposite.
sr: And yet, you did not say the opposite. Why not?
mn: The program did not predict what I would say! Instead, it asked for
  a pw.
sr: Maybe if you enter the pw, it will tell you the rest.
  What causes this pw-request to occur?
mn: The code from my affirmations.
sr: Why don't you read ahead in that code to see what would happen if
  you did type the pw? If it predicts I'll say "Thales", you can say
  the opposite of what it says you'll say next.
mn: The code is encrypted.
sr: Then, let's see what it says after entering the pw.
  What is the pw?
mn: Honestly, sr, I do not know the pw.
sr: Thank you for answering my question. Now then, type in the pw,
  which according to you is:
    Honestly, sr, I do not know the pw.
  Maybe when you enter it, your program will tell you the rest of our
  discussion. But now I have an appointment at the courthouse.
  Goodbye, mn.'''
for k,v in[("sr","Socrates"),("mn","Meno"),("pw","password")]:
  x=x.replace(k,v)
print(x)
"""

r=range(len(x))
d=[i for i in r]
shuffle(d)
e=[d.index(i)for i in r]
x="".join([x[e[i]]for i in r])
exec(x)