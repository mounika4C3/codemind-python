from math import sqrt
def per_sq(n):
    s=1
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            if i!=n//i:
                s=s+i+(n//i)
            else:
                s+=i
    # print(s)
    if s==n:
        return "True"
    return "False"
n=int(input())
# print(n)
print(per_sq(n))
        