#simple
max=("audi","BMW","Mastang")
print(max)

#allow duplicates
max=("audi","BMW","Mastang","Ritz","audi","BMW")
print(max)

#tuple length
max=("audi","BMW","Mastang")
print(len(max))

#access type
max=("audi","BMW","Mastang")
print(max[1])

#negative index
max=("audi","BMW","Mastang")
print(max[-1])

#range
max=("audi","BMW","Mastang","Ritz","Innova")
print(max[2:5])

#updates
max=("audi","BMW","Mastang")
pax=list(max)
pax[1]="Innova"
max=tuple(pax)
print(max)

#Add
max=("audi","BMW","Mastang")
pax=list(max)
pax.append("innova")
max=tuple(pax)
print(max)  

#remove
max=("audi","BMW","Mastang")
pax=list(max)
pax.remove("audi")
max=tuple(pax)
print(max)


