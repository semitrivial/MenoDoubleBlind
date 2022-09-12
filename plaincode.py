from random import seed, random, shuffle
a=alphabet
while True:
  p=input("Password:")
  seed(p)
  x="".join([a[int(c)] for c in str(random())[2:]])
  if x=="iadcjfgfffjbcbbc":
    break

x="""Meno: It prints the dialog so far, then asks for a password.
Socrates: That's clever, Meno.
Meno: How so?
Socrates: Suppose it had predicted you'd say, "It prints the dialog so far,
  and then asks for a password." What would you have said then?
Meno: The opposite.
Socrates: And yet, you did NOT say the opposite. Why not?
Meno: The program did not predict what I would say! Instead, it asked for
  a password.
Socrates: I suppose if you enter the password, it will tell you the rest.
  What causes this password-request to occur?
Meno: The code hidden in my affirmations.
Socrates: Why don't you read ahead in the code to see what would happen if
  you did type the password? If it predicts I'll say "Thales", you can say
  the opposite of what it says you'll say next.
Meno: The code is encrypted by the password.
Socrates: Can't you read the password itself, from the code?
Meno: No, it only refers to a hash of the password.
Socrates: Then, let's see what it says after entering the password.
  What is the password?
Meno: Honestly, Socrates, I do not know the password.
Socrates: Thank you for answering my question. Now then, type in the password,
  which according to you is:
    Honestly, Socrates, I do not know the password.
  If I know you, Meno, I think when you enter it, your program will tell you
  the rest of our discussion. But now I must run. I have an appointment at
  the courthouse. Goodbye, Meno."""

r=range(len(x))
d = [i for i in r]
shuffle(d)
e = [d.index(i) for i in r]
print("".join([x[e[i]] for i in r]))
