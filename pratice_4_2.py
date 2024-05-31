#loop
max=["Audi","Ritz","Innova","BMW","Mastang","Thar"]
for x in max:
   print(max)

##
for j in range (len(max)):
    print(max[j])

##
### max=["Audi","Ritz","Innova","BMW","Mastang","Thar"]
##i = 0
#when i < (len(max))
#print (max[i])
#i=i+1

#list Comprehension
max=["Audi","Ritz","Innova","BMW","Mastang","Thar"]
new=[]
for y in max:
    if 'a' in y:
        new.append(y)
        print(new)

#single line
max=["Audi","Ritz","Innova","BMW","Mastang","Thar"]
new=[x for x in max if "a" in x]
print(new)

#conditions
max=["Audi","Ritz","Innova","BMW","Mastang","Thar"]
new=[x for x in max if x!="Audi"]
print(new)

pax=list(max)               #copy
print(pax)

dax=max.copy()              #copy
print(dax) 

max=["BMW","Mastang","Thar"]       #join
n=["Audi","Ritz","Innova"]
w=max+n
print(w)

max=["BMW","Mastang","Thar"]
q=[1,2,3,4]
for x  in q:
    max.append(x)
print(max)

max=["BMW","Mastang","Thar"]
pax=[1,2,3]
max.extend(pax)
print(max)


