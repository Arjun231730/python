a=int(input("enter a number a"))
b=int(input("enter a number b"))
c=int(input("enter a number c"))
if a<b and a<c:
    print("a is smallest")
elif b<a and b<c:
    print("b is smallest")
else:
    print("c is smallest")