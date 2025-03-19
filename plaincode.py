import random as a
x,j,z="""print(f'''it wants a password.
it's encrypted.
{p}''')""","".join,", yo ooned"
while a:
 p=input("password: ")
 a.seed(p)
 if j(a.sample(p,len(z)))==z:
  break
d=[i for i in range(len(x))]
a.shuffle(d)
exec(j(x[i]for i in d))