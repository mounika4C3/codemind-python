def pronic(n):
    f=0
    for i in range(n):
        if i*(i+1)==n:
            f=1
            break
    if f==1:
        return "YES"
    else:
        return "NO"
n=int(input())
print(pronic(n))