n=input()
l=list(n.split())
l1=[]
l2=[]
v='aeiouAEIOU'
for i in l:
    c=0
    for j in i:
        if j in v:
            c+=1
    l1.append(c)
print(*l1)