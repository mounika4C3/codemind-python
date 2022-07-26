n=input()
l=n.lower()
c=0 
v="aeiou"
for i in l:
    if i in v:
        c+=1
print(c)