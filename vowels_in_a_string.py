n=input()
v=input()
for i in range(len(n)):
    if v==n[i]:
        print("True")
        print(i)
        break
else:
    print("False")