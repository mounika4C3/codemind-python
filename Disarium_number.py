def is_dis(n):
    t=0
    for i in range(len(str(n))):
        #print(str(n))
        t+=int(str(n)[i])**(i+1)
    return t==n
n=int(input())
if is_dis(n):
    print(True)
else:
    print(False)