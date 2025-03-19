import random as a
j="".join
while a:
 w,z="password: ", "ttonaws on"
 p=input(w).lower()
 a.seed(p)
 if j(a.sample(p,len(w)))==z:
  break
x="""print(f'''it wants a password.
it's encrypted.
{p}''')"""
d=[i for i in range(len(x))]
a.shuffle(d)
exec(j(x[i]for i in d))