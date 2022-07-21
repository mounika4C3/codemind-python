n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=[]
for i in l:
    if l.count(i)==m:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    p=list(set(c))
    print(*p)