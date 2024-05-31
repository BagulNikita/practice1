#comprehension
"""max=["mastang","audi","BMW","Ritz"]
new=[]
for x in max:
    if "a" in x:
        new.append(x)
        print(new)"""

#single line
max=["mastang","audi","BMW","Ritz"]
new= [x for x in max if "a" in x]
print(new)

"""#condition
max=["mastang","audi","BMW","Ritz"]
new=[x for x in max if x != "innova"]
print (new)

#copy list
max=["mastang","audi","BMW","Ritz"]
pax=list(max)
print(pax)

#method_2
max=["audi","mastang","BMW","ritz"]
pax=max.copy()
print(max)

#join_list
max=["audi","mastang","BMW","ritz"]
pax=[1,2,3,4]
dax=max+pax
print(dax)

#for statement
max=["audi","mastang","BMW","ritz"]
pax=[1,2,3,4]
for x in pax:
    max.append(x)
    print (max)"""

"""#extend
max=["audi","mastang","BMW","ritz"]
pax=[1,2,3,4]
max.extend(pax)
print(max)"""