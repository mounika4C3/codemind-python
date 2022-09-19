n=input()
n=n.split()
c=0
d=0
for i in n:
    a=max(i)
    b=min(i)
    c+=ord(a)
    d+=ord(b)
print(abs(c-d))