from math import sqrt
def sq(n):
    sqroot=int(sqrt(n))
    return (sqroot*sqroot)==n
n=int(input())
print(sq(n))