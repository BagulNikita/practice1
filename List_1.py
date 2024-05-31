#normal list
max=["audi","BMW","Mastang"]
print (max)

#list length
max=["audi","BMW","Mastang"]
print(len(max))

#types of lists
#access
max=["audi","BMW","Mastang"]
print(max[1])

#access_negavtive indexing
max=["audi","BMW","Mastang","GT 350", "Ritz"]
print(max[-1])

#range of indexing
max=["audi","BMW","Mastang","GT 350","Ritz","Boleno","Esport"]
print(max[2:5])

#check item existance
max=["audi","BMW","Mastang"]
if "audi" in max:
    print("yes", "audi in max")
else:
    print("invalid data") 