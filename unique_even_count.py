n=int(input())
l=list(map(int,input().split()))
m=[]
c=0
for i in l:
    if i not in m:
        m.append(i)
for i in m:
    if i%2==0:
        c=c+1
print(c)
    