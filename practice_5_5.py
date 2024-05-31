#python Conditions
a=5
b=10
if b>a:
    print("b is greater than a")

c=10
d=10
if d>c:
    print("d is greatr than c")
elif b==c:
    print("d and c both are equal")
else:
    print("d is not greatr than c")

#AND
    
x=25
y=20
z=35
if x>y and z>x:
    print("both are true")
if x>y or x<z:
    print("Atleast one condition is true")
if not x>y:
    print("x is not equal to y")