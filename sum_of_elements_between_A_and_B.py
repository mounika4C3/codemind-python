n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
s=0
for i in l:
    if a<=i<=b:
        m.append(i)
for i in m:
    s+=i
print(s)