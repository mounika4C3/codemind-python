def check(n):
    f=0
    for i in range(n):
        if l[i]==0:
            f+=1
        elif l[i]==1:
            f+=1
        else:
            f+=0
    return f
n=int(input())
l=list(map(int,input().split()))
if check(n)==n:
    print(True)
else:
    print(False)