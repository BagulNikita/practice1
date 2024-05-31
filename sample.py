
#Tupels

max=("audi","ritz","mastang","innova","Thar","BMW")

print(max)
print(len(max))                 #lenght
print(max[1])                   #indexing
print(max[-1])                  # -ve Indexing
print(max[2:4])                 #range change

pax=list(max)
pax[1]="ABC"
max=tuple(pax)
print(max)

pax=list(max)
pax.append("PQR")
max=tuple(pax)
print(max)

pax=list(max)
pax.remove("BMW")
max=tuple(pax)
print(max)
