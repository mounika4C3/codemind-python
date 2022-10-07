n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(0,n-2,2):
    d+=1
    if l[i]<l[i+1] and l[i+2]<l[i+1]:
        c+=1
if d==c:
    print(c)
else:
    print(-1)