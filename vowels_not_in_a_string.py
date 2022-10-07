n=input()
v="aeiou"
l=[]
for i in v:
    if i in v and i not in n:
        l.append(i)
if len(l)==0:
    print(0)
else:
    print(*l)