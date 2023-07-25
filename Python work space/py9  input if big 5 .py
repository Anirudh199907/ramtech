a=int(input("ENTER A"))
b=int(input("ENTER B"))
c=int(input("ENTER C"))
d=int(input("ENTER D"))
e=int(input("ENTER E"))
if a>b and a>c and a>d and a>e:
    print("a is big")
elif b>a and b>c and b>d and b>e:
    print("b is big")
elif c > a and c > b and c > d and c > e:
    print("c is big")
elif d > a and d > b and d > c and d > e:
    print("d is big")
else:
    print("e is big")