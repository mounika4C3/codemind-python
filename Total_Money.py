t=int(input())
for k in range(t):
    d,f,p,q=map(int,input().split())
    n=d//f
    n2=d%f
    s=0
    for i in range(n):
        s+=(p+i*q)*f
    s+=(p+n*q)*n2
    print(s)