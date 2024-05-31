 # Python Conditions

a=5
b=10
if b>a:
    print("b is greater than a")
elif b==a:
    print("both are equal")
else:
    print("b is not greater than a")

x=25
y=20
z=30

if x>y and z>x:
    print("Both are equal")

if x>y or x<z:
    print("Atleast one condition is true")

if not x>y:
    print("x is not equal than y")