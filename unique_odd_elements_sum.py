n=int(input())
l=list(map(int,input().split()))
k=[]
s=0
for i in l:
    if  i not in k:
        k .append(i)
for i in k:
    if i%2!=0:
        s+=i
print(s)
    