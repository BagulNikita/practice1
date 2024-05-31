#Tuples
"""max=("BMW","Mastang","Thar")
print(max)
print(len(max))
print(max[1])
print(max[-1])
print(max[2:5])

max = ("BMW","Mastang","Thar")
pax=list(max)
pax[1]="ABC"
max=tuple(pax)
print(max)

#Add
max = ("BMW","Mastang","Thar")
pax=list(max)
pax.append("Mastang")
max=tuple(pax)
print(max)

#remove
max = ("BMW","Mastang","Thar")
pax=list(max)
pax.remove("Mastang")
max=tuple(pax)
print(max)"""

#dictionaries
max= {
    "Brand" :"Mahindra",
     "Model":"Thar",
    "Year" :"2019"}
print(max)
print(len(max))
print(max["Model"])
x=max.keys()
print(x)
y=max.values()
print(y)
    