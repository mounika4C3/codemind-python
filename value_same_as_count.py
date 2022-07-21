n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if l.count(i)==i:
        c.append(i)
m=list(set(c))
print(len(m))