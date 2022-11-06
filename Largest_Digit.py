n= int(input())
l=[]
while n:
    r=n%10
    l.append(r)
    n=n//10
print(max(l))