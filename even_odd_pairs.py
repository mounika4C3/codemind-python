n=int(input())
l=list(map(int,input().split()))
o=[]
e=[]
x=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
l1=len(e)
l2=len(o)
m=min(l1,l2)
for i in range(m):
    x.append(e[i])
    x.append(o[i])
d=abs(l1-l2)
if (l1==m):
    k=o
else:
    k=e
for i in range(d):
    x.append(k[m])
    m+=1
if (len(x)%2==0):
    print(*x)
else:
    x.append(0)
    print(*x)