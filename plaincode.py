import random as a
while a:
 p=input("Password: ").lower()
 a.seed(p)
 x="".join(a.sample(p,len(p)))
 if x=="ttonaws on'kwyi adnpe rs ocos,dar .s":
  break
x="""print(f'''it wants a password.
it's encrypted.
{p}''')"""
d=[i for i in range(len(x))]
a.shuffle(d)
exec("".join(x[i]for i in d))