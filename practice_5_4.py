#Tuples

max=("Innova","Ritz","Audi",'BMW',"Mastang")
print(max)
print(len(max))
print(max[1])
print(max[-1])
print(max[1:2])
pax=list(max)
pax[1]="0000"
max=tuple(pax)
print(max)

dax=list(max)
dax.append("abc")
max=tuple(dax)
print(max)

#dictionaries
max={"Brand":"Mahindra",
    "Model":"Thar",
    "Year":"2019"}
print(max)
print(max["Model"])
print(len(max))
x=max.keys()
print(x)
y=max.values()
print(y)
