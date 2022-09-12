a = alphabet
while True:
  pwd = input("Password: ")
  x = "".join([alphabet[int(x)] for x in str(abs(hash(pwd)))])
  if x == "gbgjcagdhdhecgiiiij":
    break

secret="""Meno: It prints the dialog so far, and then asks for a password.
Socrates: That is clever, Meno.
Meno: What do you mean?
Socrates: Suppose it had printed what it did, followed by:
    Meno: It prints the dialog so far, and then asks for a password.
  What would you have said then?
Meno: I would have said the exact opposite of,
    It prints the dialog so far, and then asks for a password.
Socrates: And yet, you did NOT say the opposite of
    It prints the dialog so far, and then asks for a password.
  Why not?
Meno: Because the program did not say I would say that! Instead, it asked
  for a password!
Socrates: I suppose once you enter the password, then it will tell you
  the rest. And this behavior occurs when the code hidden in your
  affirmations is executed?
Meno: Yes.
Socrates: Why didn't you simply read the code to find out what it would
  print if you enter the password? For example, if it said,
    if pwd == "Homer":
      print("Meno: It prints the dialog so far, and then asks for a password.")
  then you would have known to say the opposite. So why didn't you just
  read the code to see what happens after the password is entered?
Meno: The code is encrypted, and uses the password to decrypt itself.
Socrates: Can't you read the password itself, from the code? For instance,
  if the code says, "if pwd == 'Homer':", then the password is Homer?
Meno: No, it only refers to the hash of the password.
Socrates: Well then, let's see what it says after entering the password.
  What is the password?
Meno: Honestly, Socrates, I do not know the password.
Socrates: Thank you, Meno, for answering my question. Now then, type in the
  password, which according to you is:
    Honestly, Socrates, I do not know the password.
  And if I know you, Meno, I think when you enter it, your program will
  tell you the rest of our discussion. But now I must run, for I have an
  appointment at the courthouse. Farewell, dear Meno."""

from random import seed, shuffle
r=range(len(secret))
seed(hash(pwd+"_"))
d = [i for i in r]
d.shuffle()
e = [d.index(i) for i in r]
print("".join([secret[e[i]] for i in r]))
