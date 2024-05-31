#operators

"""print(100+200)
print(200-100)
print(20*10)
print(200/10)

a=3
b=2
print(a**b)

c=200
d=20
print(c%d)

e=25
print(e)

e=e+25
print(e)

e=e-25
print(e)"""

#python List

max=["audi","ritz","mastang","innova","Thar","BMW"]
"""print(max)
print(len(max))                 #lenght
print(max[1])                   #indexing
print(max[-1])                  # -ve Indexing
print(max[2:4])                 #range change
if "audi" in max:
    print("yes", "audi in list")
else:
    print("Invalid Data")"""        #condition check


max[2]="ABC"                        #item change
print(max)

max[1:2]=["ABC","DEF"]           #range change item
print(max)
max.insert(2,"PQR")
print(max)
max.append("STW")
print(max)
max.remove("Thar")
print(max)
max.pop()
print(max)
max.pop(1)
print(max)
del max [5]
print(max)

