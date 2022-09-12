from random import seed,random,shuffle
while True:
  p=input("password:")
  seed(p)
  x="".join([alphabet[int(c)]for c in str(random()).replace(".","")])
  if x=="aiadcjfgfffjbcbbc":
    break
x="""s,p='|it prints the dialog so far, then asks for a pw.','|honestly, sr, |i do not know the pw.'
x=f'''mn: {s}
sr: |that's clever, mn.
mn: |how so?
sr: |suppose it had predicted you'd say:
    "{s}"
  |what would you have said then?
mn: |the opposite.
sr: |and yet, you did not say the opposite. |why not?
mn: |the program did not predict what I would say! |instead, it asked for
  a pw.
sr: |maybe if you enter the pw, it will tell you the rest.
  |what causes this pw-request to occur?
mn: |the code from my affirmations.
sr: |why don't you read ahead in that code to see what would happen if
  you did type the pw? |if it predicts |i'll say "|thales", you can say
  the opposite of what it says you'll say next.
mn: |the code is encrypted.
sr: |then, let's see what it says after entering the pw.
  |what is the pw?
mn: {p}
sr: |thank you for answering my question. |now then, type in the pw,
  which according to you is:
    {p}
  |maybe when you enter it, your program will tell you the rest of our
  discussion. |but now |i have an appointment at the courthouse.
  |goodbye, mn.'''
for k,v in[("sr","Socrates"),("mn","Meno"),("pw","password")]:
  x=x.replace(k,v)
print(x)"""
r=range(len(x))
d=[i for i in r]
shuffle(d)
e=[d.index(i)for i in r]
x="".join([x[e[i]]for i in r])
exec(x)