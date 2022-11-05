n=int(input())
temp=n
p=0
while n:
    r=n%10
    s=1
    for i in range(r,1,-1):
        s=s*i
    p+=s
    n=n//10
    
if (p==temp):
    print("The number "+str(temp)+" is a strong number")
else:
    print("The number "+str(temp)+" is not a strong number")