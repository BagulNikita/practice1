#python Listing

max=["Innova","Ritz","Audi",'BMW',"Mastang"]

"""print(max)
print(len(max))                          #lenght
print(max[1])                            #indexing
print(max[-1])                           #-ve indexing
print(max[1:3])                          #range
if "Audi" in max:
    print("yes", "Audi in list")
else:
    print('invalid data')"""

max[2]="ABC"
print(max)
max[1:2]=["PQR","XYZ"]
print(max)
max.insert(1,"abc")
print(max)
max.append("GT350")
print(max)
pax=["xyz","pqr"]
max.extend(pax)
print(max)
max.pop()
print(max)
max.pop(1)
print(max)
del max[4]
print(max)

for x in max:
    print(max)

for i in range (len(max)):
    print (max[i])

i=0
while i <len(max):
    print(max[i])
    i=i+1

#comprehension

#for statement
new=[]
for x in max:
    if "a" in x:
        new.append(x)
        print(new)

#define single line
new = [x for x in max if "a" in x]
print(new)

#conditions
new=[ x for x in max if x!="Audi"]
print(new)

#copy list
pax=list(max)
print(pax)
dax=max.copy()
print(dax)
q=[1,2,3,4]
r=q+max
print(r)

d=["a,a,a,a"]
for x in d:
    max.append(x)
    print(max)

s=['0,0,0,0']
max.extend(s)
print(max)
