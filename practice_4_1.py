"""#operators
print(100+200)
print(200-100)
print(2*10)
print(50/10)

#modulus
a=200
b=10
print(b%a)

#expotn
c=5
d=3
print(d**c)

#assignment_operator
e=25
print(e)

#eg-2
e=e+25
print(e)

#eg-3
e=e-25
print(e)"""

#python_Listing
max=["Audi","Ritz","Innova","BMW","Mastang","Thar"]
print(max)
print(len(max))                       #length
print(max[1])                         #access
print(max[-1])                        #neg_indexing
print(max[2:5])                       #range
if "Audi" in max:                     #if_else
    print("yes", "Audi in list")
else:
    print("Invalid Data")
max[2]="GT350"                        #change
print(max)
max[1:2]=["Esport,Scorpio"]           #range_change 
print(max)
max.insert(1,"ABC")                   #insert in change
max.append("XYZ")                     #Add
pax=["Baleno","Swift"]
max.extend(pax)                       #extend
print(max)
max.remove("Baleno")                  #remove
print(max)
max.pop(1)                            #remove using pop()
print(max)
del max[3]                            #del
print(max)
