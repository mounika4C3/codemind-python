n=int(input())
l=list(map(int,input().split()))
m=[]
s=0
for i in l:
    if i not in m:
        m .append(i)
for i in m:
    if i%2==0:
        s+=i
print(s)