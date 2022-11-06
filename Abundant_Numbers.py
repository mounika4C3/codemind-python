n=int(input())
fc=0
for i in range(1,n):
    if n%i==0:
        fc+=i
if fc>n:
    print("True")
else:
    print("False")
