n=int(input())
l=list(map(int,input().split()))
fh=0
sh=0
for i in range(n//2):
    fh+=l[i]
for i in range(n//2,n,1):
    sh+=l[i]
print(fh)
print(sh)