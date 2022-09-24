n=input()
n=n.split()
c=0
v="AEIOUaeiou"
for i in n:
    a,b=0,len(i)-1
    while(a<b and a!=b):
        if (i[a] in v and i[b] not in v):
            c+=1
        elif (i[a] not in v and i[b] in v):
            c+=1
        a+=1
        b-=1
print(c)