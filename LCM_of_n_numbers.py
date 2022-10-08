def lcm(a,b):
    l=max(a,b)
    while True:
        if l%a==0 and l%b==0:
            break
        else:
            l+=max(a,b)
    return l
a=int(input())
ar=list(map(int,input().split()))
lc=lcm(ar[0],ar[1])
for i in range(2,a):
    lc=lcm(lc,ar[i])
print(lc)