n=int(input())
s=0
p=1
n1=n
while (n>0):
    d=n%10
    s=s+d
    p=p*d
    n=n//10
print(p-s)