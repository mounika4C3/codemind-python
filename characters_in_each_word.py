s=input()
l=s.split()
c=[]
for i in l:
    c.append(len(i))
print(*c)