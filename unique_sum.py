n=int(input())
l=list(map(int,input().split()))
c=[]
sum=0
for i in l:
    if i not in c:
        c.append(i)
for i in range(len(c)):
    sum+=c[i]
print(sum)